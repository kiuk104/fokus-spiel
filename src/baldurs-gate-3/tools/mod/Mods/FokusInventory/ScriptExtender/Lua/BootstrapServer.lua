-- Fokus Spiel 인벤토리 자동 내보내기 (읽기 전용 — 게임 데이터를 바꾸지 않음)
-- 불러오기 · 저장 · 플레이 중 5분마다 %LocalAppData%\Larian Studios\Baldur's Gate 3\Script Extender\fokus_inventory.json 갱신
function FokusExport(reason)
  local function tsHandle(ts)
    if ts == nil then return nil end
    if type(ts) == "string" then return ts end
    local ok, h = pcall(function() return ts.Handle.Handle end)
    if ok and type(h) == "string" then return h end
    return nil
  end
  local function tsText(ts, h)
    if h then
      local ok, s = pcall(Ext.Loca.GetTranslatedString, h)
      if ok and s and s ~= "" then return s end
    end
    local ok, s = pcall(function() return ts:Get() end)
    if ok then return s end
  end
  out = { version = 6, chars = {}, errors = {} }
  DEBUG_DONE = nil
  local contents
  local function rec(e, depth)
    local r = {}
    pcall(function() r.uuid = e.Uuid.EntityUuid end)
    pcall(function()
      local dn = e.DisplayName
      r.h = tsHandle(dn.Name) or tsHandle(dn.NameKey)
      r.name = tsText(dn.Name, r.h)
    end)
    pcall(function() r.custom = e.CustomName.Name end)
    pcall(function() r.stats = e.Data.StatsId; r.weight = e.Data.Weight end)
    pcall(function() r.amount = e.ServerItem.Amount end)
    if r.amount == nil and r.uuid then pcall(function() r.amount = Osi.GetStackAmount(r.uuid) end) end
    if r.amount == nil then pcall(function()
      local q = 0; for _, en in pairs(e.InventoryStack.Entries) do q = q + en.Quantity end
      if q > 0 then r.amount = q end
    end) end
    if DEBUG_DONE == nil and r.stats == "OBJ_GoldPile" then
      DEBUG_DONE = true
      pcall(function() out.debug = { comps = e:GetAllComponentNames(false) } end)
    end
    pcall(function() r.tpl = e.ServerItem.Template.Id; r.tplName = e.ServerItem.Template.Name end)
    pcall(function() r.icon = e.Icon.Icon end)
    pcall(function()
      for _, a in pairs(e.Use.UseActions) do
        local ok, b = pcall(function() return a.BookId end)
        if ok and b and b ~= "" then r.book = b end
      end
    end)
    if r.book == nil then pcall(function()
      for _, a in pairs(e.ServerItem.Template.OnUsePeaceActions) do
        local ok, b = pcall(function() return a.BookId end)
        if ok and b and b ~= "" then r.book = b end
      end
    end) end
    pcall(function() r.rarity = e.Value.Rarity; r.value = e.Value.Value end)
    pcall(function() r.story = (e.IsStoryItem ~= nil) end)
    pcall(function() r.slot = e.InventoryMember.EquipmentSlot end)
    pcall(function() if e.Wielded then r.wielded = true end end)
    if depth < 4 and e.InventoryOwner then
      local ok, c = pcall(contents, e, depth + 1)
      r.items = ok and c or { { err = tostring(c) } }
    end
    return r
  end
  contents = function(owner, depth)
    local list = {}
    for _, inv in pairs(owner.InventoryOwner.Inventories) do
      local c = inv.InventoryContainer
      if c then
        for slot, d in pairs(c.Items) do
          local it = d.Item
          if it then
            local ok, r = pcall(rec, it, depth)
            if ok then r.s = slot else r = { err = tostring(r) } end
            list[#list + 1] = r
          end
        end
      end
    end
    return list
  end

  local seen = {}
  local function addChar(id, kind)
    local e = Ext.Entity.Get(id)
    if not e then return end
    local u; pcall(function() u = e.Uuid.EntityUuid end)
    u = u or tostring(id)
    if seen[u] then return end
    seen[u] = true
    local r = rec(e, 0); r.kind = kind
    local cs = {}
    pcall(function() cs.level = e.EocLevel.Level end)
    pcall(function() cs.hp = e.Health.Hp; cs.maxhp = e.Health.MaxHp end)
    pcall(function() cs.ac = e.Resistances.AC end)
    pcall(function() local a = {}; for i, v in pairs(e.Stats.Abilities) do a[#a + 1] = v end; cs.abilities = a end)
    pcall(function()
      local cl = {}
      for _, c in pairs(e.Classes.Classes) do
        local x = { level = c.Level, class = c.ClassUUID, sub = c.SubClassUUID }
        pcall(function() local d = Ext.StaticData.Get(c.ClassUUID, "ClassDescription"); x.className = d.Name; x.classH = tsHandle(d.DisplayName) end)
        pcall(function() local d = Ext.StaticData.Get(c.SubClassUUID, "ClassDescription"); x.subName = d.Name; x.subH = tsHandle(d.DisplayName) end)
        cl[#cl + 1] = x
      end
      cs.classes = cl
    end)
    local eq = {}
    for _, slot in ipairs({ "Helmet", "Breast", "Cloak", "Melee Main Weapon", "Melee Offhand Weapon", "Ranged Main Weapon", "Ranged Offhand Weapon", "Ring", "Ring2", "Boots", "Gloves", "Amulet", "MusicalInstrument", "MeleeMainHand", "MeleeOffHand", "RangedMainHand", "RangedOffHand" }) do
      pcall(function()
        local it = Osi.GetEquippedItem(id, slot)
        if it then local ie = Ext.Entity.Get(it); if ie then local x = rec(ie, 9); x.eqslot = slot; eq[#eq + 1] = x end end
      end)
    end
    cs.equipped = eq
    r.charStats = cs
    out.chars[#out.chars + 1] = r
  end
  local ok, err = pcall(function()
    for _, row in pairs(Osi.DB_Players:Get(nil)) do addChar(row[1], "party") end
  end)
  if not ok then out.errors[#out.errors + 1] = "players: " .. tostring(err) end
  ok, err = pcall(function()
    for _, e in pairs(Ext.Entity.GetAllEntitiesWithComponent("PartyMember")) do
      local u = e.Uuid.EntityUuid; addChar(u, "member")
    end
  end)
  if not ok then out.errors[#out.errors + 1] = "members: " .. tostring(err) end
  ok, err = pcall(function()
    for _, row in pairs(Osi.DB_PartOfTheTeam:Get(nil)) do addChar(row[1], "camp") end
  end)
  if not ok then out.errors[#out.errors + 1] = "team: " .. tostring(err) end
  ok, err = pcall(function()
    for _, e in pairs(Ext.Entity.GetAllEntitiesWithComponent("CampChest")) do
      local u = e.Uuid.EntityUuid; addChar(u, "campchest")
    end
  end)
  if not ok then out.errors[#out.errors + 1] = "camp: " .. tostring(err) end
  out.buyback = {}
  ok, err = pcall(function()
    for _, e in pairs(Ext.Entity.GetAllEntitiesWithComponent("TradeBuybackData")) do
      local ok2, r = pcall(rec, e, 9)
      if ok2 then
        pcall(function() local b = e.TradeBuybackData; r.amount = b.Amount; r.trader = rec(b.Trader, 9).name; r.buyer = rec(b.Buyer, 9).name end)
        out.buyback[#out.buyback + 1] = r
      end
    end
  end)
  if not ok then out.errors[#out.errors + 1] = "buyback: " .. tostring(err) end
  local n = 0
  local function count(l) for _, x in pairs(l or {}) do n = n + 1; count(x.items) end end
  for _, c in pairs(out.chars) do count(c.items) end
  Ext.IO.SaveFile("fokus_inventory.json", Ext.Json.Stringify(out))
  _P(string.format("[Fokus] 캐릭터 %d명 · 아이템 %d개 저장 완료 → fokus_inventory.json", #out.chars, n))

end

local function safeExport(reason)
  local ok, err = pcall(FokusExport, reason)
  if not ok then Ext.Utils.PrintWarning("[Fokus] 내보내기 실패: " .. tostring(err)) end
end

local running = false
local function tick()
  if not running then return end
  safeExport("timer")
  Ext.Timer.WaitFor(300000, tick)
end

Ext.Events.GameStateChanged:Subscribe(function(e)
  if e.ToState == "Save" then safeExport("save") end
  if e.ToState == "Running" and not running then
    running = true
    Ext.Timer.WaitFor(8000, function() safeExport("load") end)
    Ext.Timer.WaitFor(300000, tick)
  end
  if e.ToState == "UnloadSession" or e.ToState == "Exit" then running = false end
end)

Ext.RegisterConsoleCommand("fokus", function() safeExport("console") end)
