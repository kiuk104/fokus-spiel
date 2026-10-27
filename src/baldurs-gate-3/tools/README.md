# BG3 인벤토리 목록 도구

1. 게임 `bin/ScriptExtenderSettings.json` 에 `"CreateConsole": true` (콘솔 창 켜기)
2. `fokus_inv.lua` 를 `%LocalAppData%\Larian Studios\Baldur's Gate 3\Script Extender\` 에 두고,
   게임 콘솔(S >>)에서 `load(Ext.IO.LoadFile("fokus_inv.lua"))()` → 같은 폴더에 `fokus_inventory.json`
3. 이름표 `loca.pkl` 만들기: `lspk.py` 로 `Data/Localization/English.pak`, `Korean/Korean.pak` 를 풀고
   english.loca · korean.loca 를 handle→문장 dict 로 저장 (모드 가방 이름은 `loca.json`)
4. 아이콘: `Data/Game.pak` 의 `Public/Game/GUI/Assets/ControllerUIIcons/items_png/<icon>.DDS` → 64px PNG → `baldurs-gate-3/icons/items/`
5. `python make_inventory.py fokus_inventory.json <날짜> <아이콘폴더> inv_section.md` → guide.md 의 "📦 지금 들고 있는 아이템" 섹션 교체
