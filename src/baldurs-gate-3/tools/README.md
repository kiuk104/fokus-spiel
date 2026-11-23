# BG3 인벤토리 목록 도구

1. 게임 `bin/ScriptExtenderSettings.json` 에 `"CreateConsole": true` (콘솔 창 켜기)
2. `fokus_inv.lua` 를 `%LocalAppData%\Larian Studios\Baldur's Gate 3\Script Extender\` 에 두고,
   게임 콘솔(S >>)에서 `load(Ext.IO.LoadFile("fokus_inv.lua"))()` → 같은 폴더에 `fokus_inventory.json`
3. 이름표 `loca.pkl` 만들기: `lspk.py` 로 `Data/Localization/English.pak`, `Korean/Korean.pak` 를 풀고
   english.loca · korean.loca 를 handle→문장 dict 로 저장 (모드 가방 이름은 `loca.json`)
4. 아이콘: `Data/Game.pak` 의 `Public/Game/GUI/Assets/ControllerUIIcons/items_png/<icon>.DDS` → 64px PNG → `baldurs-gate-3/icons/items/`
5. `python make_inventory.py fokus_inventory.json <날짜> <아이콘폴더> inv_section.md` → guide.md 의 "📦 지금 들고 있는 아이템" 섹션 교체

## 자동 내보내기 모드 (2026-10-27~)
- `mod/Mods/FokusInventory/` → `python pakw.py mod FokusInventory.pak` → 게임 Mods 폴더 + BG3 Mod Manager 에서 활성화
- 불러오기 8초 뒤 · 저장할 때 · 5분마다 `fokus_inventory.json` 자동 갱신 (콘솔 명령 `!fokus` 도 가능)
- 판매 기록: `python make_inventory.py <json> <날짜> <아이콘> inv.md inventory_history.json party.md books.md`
  — `inventory_history.json` 에 uuid 별로 쌓고, 사라진 아이템은 판매됨(🔴 판정이었거나 되사기 목록) / 없어짐 으로 표시
- 책 본문: `Data/Gustav.pak` 등의 `Localization/*Books*.lsf` (BookId → 본문 handle) → `books.pkl`

## 이름표 · 책 본문 보관 위치 (2026-11-23~)
- `loca.pkl`(한글·영문 이름표) · `books.pkl`(BookId → 본문 handle)은 git 에 넣지 않고 PC 의
  `%LocalAppData%\Larian Studios\Baldur's Gate 3\Script Extender\` 에 둔다. 갱신할 때 이 둘을 `tools/` 로 가져와 실행.
- `loca.pkl` 이 없으면 `make_inventory.py` 는 한영 병기 모드 이름("한글 (English)")에서 이름을 나눠 쓴다(책 섹션은 생략).
- 다시 만들기: `Localization/English.pak` · `Korean/Korean.pak` 의 `english.loca` · `korean.loca`,
  책은 `*Books*.lsf` 에서 "handle\0 … BookId\0" 순서로 짝을 찾는다(Content 가 UUID 앞에 온다).
- 아이콘: `Game.pak` 의 `ControllerUIIcons/items_png/<icon>.DDS` → 64px PNG. BagsBagsBags 가방 아이콘은 모드 pak 에 있어 빠져 있다.
