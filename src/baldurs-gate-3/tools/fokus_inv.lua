-- Fokus Spiel: 파티 인벤토리를 fokus_inventory.json 으로 내보내기 (읽기 전용)
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
out = { version = 2, chars = {}, errors = {} }
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
  pcall(function() r.rarity = e.Value.Rarity; r.value = e.Value.Value end)
  pcall(function() r.story = (e.IsStoryItem ~= nil) end)
  pcall(function() r.slot = e.InventoryMember.EquipmentSlot end)
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
  for _, e in pairs(Ext.Entity.GetAllEntitiesWithComponent("CampChest")) do
    local u = e.Uuid.EntityUuid; addChar(u, "campchest")
  end
end)
if not ok then out.errors[#out.errors + 1] = "camp: " .. tostring(err) end
local n = 0
local function count(l) for _, x in pairs(l or {}) do n = n + 1; count(x.items) end end
for _, c in pairs(out.chars) do count(c.items) end
Ext.IO.SaveFile("fokus_inventory.json", Ext.Json.Stringify(out))
_P(string.format("[Fokus] 캐릭터 %d명 · 아이템 %d개 저장 완료 → fokus_inventory.json", #out.chars, n))
