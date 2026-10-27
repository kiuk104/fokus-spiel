# 발더스 게이트 3 모험 노트

> 📝 개인 모험 노트예요. 막힌 부분을 질문하면 답과 진행 결과가 여기에 Q1, Q2… 순서로 쌓여요.
>
> 🎮 플레이어: 초보자 · 와우 / 엘더스크롤 / 드래곤에이지 취향 · 스토리와 동료 관계 중심

---

# 🖥️ PART 1 — 기술 세팅

## 세이브 · 설정

- **빠른 저장은 F5.** 주사위 판정이 걸린 대화나 큰 전투 전에는 꼭 저장. 실패하면 불러와도 괜찮아요.
- **난이도**: 탐험가(쉬움) 또는 균형(보통) 추천. 설정에서 언제든 바꿀 수 있어요.

## 그래픽 · 컨트롤러 세팅

아직 기록이 없어요.

## 모드 구성 (BG3 Mod Manager · Vortex)

- 모드는 **BG3 Mod Manager**로 순서를 정하고 **Save → Export** 해야 게임에 반영돼요. 노란 번개 아이콘 = Script Extender 필요.
- **빨간 줄** = 필요한 모드(의존성) 문제. 예: Gale's beard Fix는 **NF_GaleModsCore보다 아래**에 있어야 함.
- **가방 모드는 하나만.** BagsBagsBags · BagsBagsBagsReforged · Autosort Containers 를 같이 켜면 같은 물건을 서로 끌어가요. → Autosort Containers 제거(2026-10-26).
- ⚠️ **아이템을 추가하는 모드는 플레이 도중에 빼면 그 아이템과 안의 내용물이 사라져요.** 이번 세이브는 BagsBagsBags(원조)를 끄면 Reforged 가방에 옮긴 물건까지 사라져서 **원조 + Reforged 둘 다 유지**. 넣고 빼는 건 새 게임 시작할 때만.
- 모드 파일 위치: `%LocalAppData%\Larian Studios\Baldur's Gate 3\Mods` (Vortex 바로가기 → 원본은 `E:\SteamLibrary\steamapps\common\Baldurs Gate 3\<모드 폴더>`)

---

# 🎮 PART 2 — 게임플레이 가이드

## 캐릭터 · 빌드

### 📊 파티 현황판 (2026-09-27 · 전원 4레벨)

| 캐릭터 | 클래스 | 와우식 역할 | 주 능력치 | HP | 방어도 | 상태 |
|---|---|---|---|---|---|---|
| **Wyll** (주인공) | 하프오크 팔라딘 · 선조의 맹세 | 탱커 겸 근접 딜러 | 근력 18 · 매력 15 | 32 | 16 | ✅ 능력치 양호 |
| **섀도하트** | 하이 하프엘프 클레릭 · 기만 권역 | 힐러 · 버프 | 지혜 **17** | 31 | 16 | ⚠️ 원거리 무기 없음 |
| **게일** | 인간 위저드 · 방출술 | 원거리 광역 딜러 | 지능 **17** | 26 | **11** | 🚨 방어도 매우 낮음 |
| **아스타리온** | 하이 엘프 로그 · 비전 괴도 | 딜러 · 자물쇠/함정 | 민첩 **17** | 31 | 14 | ⚠️ 장신구 슬롯 빔 |

야영지: 라에젤, 카를라크, 위더스(리스펙 가능)

### ⚠️ 공통 문제: 4레벨 특기 선택

동료 3명 모두 4레벨 특기를 비효율적으로 골라 주 능력치가 **홀수(17)** 로 남아 있어요. **능력치 향상(+1/+1)** 을 골랐다면 18이 되어 명중·주문 DC·피해가 전부 1씩 올라가요.

→ 야영지 **위더스에게 100골드**를 내면 재분배(리스펙) 가능. 안 해도 클리어엔 지장 없는 **최적화 항목**이에요.

| 우선순위 | 캐릭터 | 리스펙 방향 | 효과 |
|---|---|---|---|
| 1 | 게일 | 지능 +1, 민첩 +1 | 명중·주문 DC·방어도 |
| 2 | 섀도하트 | 지혜 +1, 민첩 +1 | 치유량·주문 DC·방어도 |
| 3 | 아스타리온 | 민첩 +1, 지혜 +1 | 명중·피해·감지 |

### 캐릭터별 성장 방향

**Wyll (팔라딘)**
- 양손 무기 + 방어술 조합 무난. 5레벨 **추가 공격**이 핵심.
- 주문 슬롯은 치명타가 났을 때 **신성 강타**용으로 아껴두기.
- 8레벨 특기 추천: **대형 무기의 달인**.
- 방어도 보강은 그림포지 **아다만틴 갑옷**으로.

**게일 (위저드)**
- 인간이라 **경갑·방패 숙련**만 있음(평갑·중갑은 불가). **방패 하나(+2)** 가 가장 싸고 효과 큼 → 방어도 13. 마법사 갑옷 주문과 함께면 16.
- 위저드 두루마리는 게일에게 몰아주고 주문서로 학습(골드 필요).
- 5레벨 추천 주문: **화염구**, **가속**.

**아스타리온 (로그)**
- 하이 엘프라 **장궁 숙련** → 단궁 대신 장궁.
- 투구·망토·장갑·장신구 슬롯이 비어 있음.
- 자물쇠 따기·함정 해제·은신 담당.

**섀도하트 (클레릭)**
- 원거리 무기 없음 → 경쇠뇌나 단궁 지급.
- 5레벨 **영혼 수호자** 필수. 전투 시작하자마자 켜고 적 사이로.
- **흔적 없는 이동**으로 파티 전체 은신 보너스.

## 동료 · 캠프

### 파티 상성

탱커·힐러·딜러·도적이 한 명씩 있는 **정석 파티**. 바꿀 필요 없음.

- **전열이 Wyll 한 명뿐** → 섀도하트를 반 전열로(영혼 수호자), 게일은 반드시 뒤에.
- **치유가 섀도하트에게 몰림** → 게일에게 회복의 애뮬릿, Wyll의 신앙 치유(Lay on Hands), 물약 분산.
- **대화 판정은 Wyll** (매력 최고). 기만만 아스타리온.
- 그림포지 보스전이 부담되면 게일 대신 카를라크 투입도 가능.

### 🔎 판정 담당표

| 판정 | 담당 |
|---|---|
| 비전 · 역사 · 조사 | 게일 (+5) |
| 종교 · 통찰 | 섀도하트 또는 게일 |
| 설득 · 위협 | Wyll |
| 기만 | 아스타리온 |
| 자물쇠 · 함정 · 은신 | 아스타리온 |
| 감지 | 섀도하트 |

### 💍 목걸이 배분

| 아이템 | 효과 | 누구에게 |
|---|---|---|
| **회복의 애뮬릿** (희귀) | 치유의 단어 + 다중 치유의 단어 | **게일** — 보조 힐러 |
| **절대자의 호부** (고급) | 지원(Aid) 주문 + 죽음 내성 유리 | **Wyll** — 황동 로켓과 교체 |
| **실격자의 애뮬릿** (고급) | 참격 저항 · 타격 취약 | **게일에게 먹이기** (개인 퀘스트 "!") |
| 황동 로켓 · 빛바랜 로켓 | 효과 없음 (이야기 아이템) | 야영지 상자 보관, 팔지 말 것 |

### 초보자 팁 (와우 · 엘더스크롤 유저용)

- **턴제는 자리 잡기가 전부.** 전투 전에 배치하고, 궁수와 게일은 **높은 곳**에.
- **은신 상태에서 선공**으로 전투를 열면 훨씬 유리.
- **소모품을 아끼지 말 것.** 치유 물약은 **던지면** 멀리 있는 동료도 회복.
- **긴 휴식은 자주 해도 됨.** 야영 대화(드래곤에이지 캠프 대화 같은 것)가 진행됨.
- **밀치기**로 절벽·물가의 적을 떨어뜨리면 한 방. 언더다크는 낭떠러지가 많아요.
- 야영지에서 **"!" 뜬 동료**는 꼭 말 걸기. 이 게임의 진짜 재미는 동료 서사와 로맨스.

## 🎒 인벤토리 · 가방 정리

### 이름이 섞여 보이는 이유

가방 모드가 두 개라서 **같은 용도의 가방이 2개씩** 생겨요.
- **영어 이름 가방** = 원조 **BagsBagsBags** (한글화 없음)
- **한글 이름 가방** = **BagsBagsBagsReforged** (+ 한글화 모드)

자동 분류는 **파티원 인벤토리에 있는 가방만** 작동해요. 같은 용도 가방은 하나만 몸에 들고, 짝꿍은 **여행용 궤짝**에 빈 채로 넣어두면 서로 물건을 뺏지 않아요.

### 📖 가방 한영 대조표

같은 줄 = 같은 용도. ⚙️ = 자동 분류(주우면 알아서 들어감), ✋ = 직접 넣기. 한글·영문 이름과 아이콘은 설치된 모드 파일에서 그대로 뽑았어요. 원조 BagsBagsBags 아이콘은 아직 없어요.

| 용도 | Reforged 한글 이름 | Reforged 영문 이름 | 원조 BagsBagsBags (영문) |
|---|---|---|---|
| **물약** | <img src="icons/PotionBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">차가운 물약 상자 ⚙️ | Chilled Potion Crate | Potion Pouch ⚙️ |
| **두루마리** | <img src="icons/ScrollBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">실룬의 두루마리 통 ⚙️ | Syluné's Scroll Case | Scroll Case ⚙️ |
| **화살 · 탄환(볼트)** | <img src="icons/ArrowBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">자론다르의 화살통 ⚙️ | Zarondar's Quiver | Arrows ⚙️ |
| **수류탄 · 폭발물** | <img src="icons/GrenadeBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">자카라 연금술사의 가방 ⚙️ | Zakharan Alchemist's Satchel | Grenade Satchel ⚙️ |
| **독 · 무기 도포제** | <img src="icons/CoatingBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">암살자의 허리띠 ⚙️ | Assassin's Belt | Weapon Coatings ⚙️ |
| **책 · 메모 · 편지** | <img src="icons/BookBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">무한 책장 ⚙️ | The Infinite Bookcase | Books ⚙️ |
| **염료** | <img src="icons/DyeBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">흑목 염료 상자 ⚙️ | Darkwood Dye Chest | Dye sack ✋ |
| **야영지 복장 · 속옷** | <img src="icons/ClothingBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">의류 진열장 ⚙️ | Clothing Display Case | Clothes Bundle ✋ |
| **금화 · 귀금속** | <img src="icons/ValuableBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">'아바토르의 베인' 금고 ⚙️ | 'Abbathor's Bane' Strongbox | Valuables ✋ |
| **장비 (무기·방패·투구·갑옷·장갑·망토·장화)** | <img src="icons/MeleeBag.png" width="24" height="24" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px"><img src="icons/ShieldBag.png" width="24" height="24" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px"><img src="icons/RangedBag.png" width="24" height="24" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px"><img src="icons/HelmBag.png" width="24" height="24" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px"><img src="icons/ArmorBag.png" width="24" height="24" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px"><img src="icons/GloveBag.png" width="24" height="24" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px"><img src="icons/CloakBag.png" width="24" height="24" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px"><img src="icons/BootBag.png" width="24" height="24" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px"><br>모덴카이넨의 에테르 무기고 ✋ (근거리·방패·원거리·투구·갑옷·장갑·망토·장화 — 이름은 같고 아이콘 테두리 색이 달라요) | Mordenkainen's Aetherial Armory | Weapon bag · Shield bag · Helm bag · Armor bag · Gloves bag · Cloak bag · Boots bag ✋ |
| **보석 (반지·목걸이)** | <img src="icons/JewelryBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">딥윈터의 보석함 ✋ | Deepwinter's Jewelcase | Jewellery Case ✋ |
| **퀘스트 물품** | <img src="icons/QuestBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">세 가지 운명의 가방 ✋ | The Bag of Threefold Fates | Quest Items ✋ |
| **여분 장비 섞어 담기** | <img src="icons/GearBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">영웅의 장비 가방 | Hero's Gear Bag | Gear ✋ |
| **기념품** | <img src="icons/KeepsakeBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">기쁨의 주머니 | Pouch of Joy | Keepsakes box ✋ |
| **잡동사니** | <img src="icons/MiscBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">철트 비늘가방 | Chultan Scalebag | Bits and bobs ✋ |
| **가방 보관용 가방** | <img src="icons/BagBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">소유의 가방 꾸러미 ✋ | Bag of Holding Bags | Bags Bag |

**Reforged에만 있는 가방**

| 용도 | 한글 | 영문 |
|---|---|---|
| 연금술 재료 | <img src="icons/AlchemyBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">아멜리오의 연금술 보관함 ⚙️ | Amelior's Alchemy Case |
| 음식 · 음료 | <img src="icons/FoodBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">하플링의 도시락 ⚙️ | The Halfling's Lunchbox |
| 포도주 · 에일 · 증류주 | <img src="icons/AlcoholBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">드워프 술장 ⚙️ | Dwarven Liquor Cabinet |
| 열쇠 | <img src="icons/KeyBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">더마토인의 열쇠고리 ⚙️ | Dumathoin's Keyring |
| 모험 도구 | <img src="icons/AdventurerBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">모험가의 배낭 ⚙️ | Adventurer's Backpack |
| 팔 물건 | <img src="icons/JunkBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">화물 상자 | Wares Crate |
| 악기 | <img src="icons/InstrumentBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">와이번스퍼의 악기 보관함 | Wyvernspur's Instrument Case |
| 가방 꾸러미 소환 반지 | <img src="icons/OrganizingRing.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">정리정돈의 네더릴 반지 | Netherese Ring of Organizing |
| 동료 전용 가방 소환 주문 | 숙명의 가방 소환 | Summon Fatebound Bag |

**동료 전용 가방** (그 동료의 여분 장비·개인 물품)

| 동료 | 한글 | 영문 |
|---|---|---|
| 윌 | <img src="icons/WyllBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">레이븐가드 상자 | Ravengard Chest |
| 섀도하트 | <img src="icons/ShadowheartBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">샤의 밤가방 | Sharran Nightbag |
| 레이젤 | <img src="icons/LaezelBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">기스양키 가죽 자루 | Githyanki Leather Sack |
| 게일 | <img src="icons/GaleBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">비전 상자 | Arcane Chest |
| 아스타리온 | <img src="icons/AstarionBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">상류층의 손가방 | Nobleman's Handbag |
| 카를라크 | <img src="icons/KarlachBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">아베르누스 영혼 상자 | Avernus Soulchest |
| 할신 | <img src="icons/HalsinBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">버크 가죽 배낭 | Buckskin Pack |
| 자헤이라 | <img src="icons/JaheiraBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">낡은 여행용 짐가방 | Worn Travel Trunk |
| 민스크 | <img src="icons/MinscBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">오래된 털가방 | Old Woolen Pack |
| 민타라 | <img src="icons/MintharaBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">베인레 거미 비단 가방 | Baenre Spidersilk Bag |

### 화면 용어

| 한글 | 영문 |
|---|---|
| 여행용 궤짝 | Traveller's Chest |
| 전부 습득 | Take All |
| 모두 표시 | Show All (인벤토리 필터) |
| 무기 도포제 | Weapon Oils / Coatings |
| 탄환 | Bolts (석궁 볼트) |

### 몸에 들고 다닐 가방 5개 (추천)

<img src="icons/PotionBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">**차가운 물약 상자** · <img src="icons/ScrollBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">**실룬의 두루마리 통** · <img src="icons/ArrowBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">**자론다르의 화살통** · <img src="icons/GrenadeBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">**자카라 연금술사의 가방** · <img src="icons/CoatingBag.png" width="32" height="32" alt="" loading="lazy" style="vertical-align:middle;margin-right:6px">**암살자의 허리띠**
- 나머지 가방은 여행용 궤짝에. 익숙해지면 연금술 재료·염료 가방을 하나씩 추가.
- 분류 안 된 물건은 **다른 동료 초상화에 끌어다 놓았다가 돌려받으면** 자동 분류가 다시 돌아요.
- 음식은 캠프로 보내면 야영 물자로 정리, 안 쓰는 장비·잡템은 팔기.

### 👀 가방 속 아이템 보는 법

여러 가방의 내용을 한 화면에 펼쳐 보는 기능은 기본 게임에 없어요.
- **소모품은 핫바 "아이템" 탭에서**: 가방 안의 물약 · 두루마리 · 화살 · 투척물이 자동으로 모여요. 가방을 열지 않고 바로 확인하고 쓸 수 있어요.
- **가방 여러 개 열기**: 가방을 하나씩 클릭하면 이미 연 창이 닫히지 않고 옆에 쌓여요. 2~3개가 적당해요.
- **Shift + 클릭**은 여러 아이템을 골라 옮기거나 팔 때만 쓸 수 있어요. 가방을 한꺼번에 여는 기능은 없어요.
- **가방 아이콘의 숫자**(예: 35, 12)는 그 가방에 든 아이템 개수예요.
- **검색창("모두 표시")**: 이름 일부를 입력하면 파티 전체에서 맞는 아이템만 보여요(예: `의식` → 의식용 무기, Q21). 가방 안까지 찾는지는 확인 필요.
- 모드: **Inventory Expanded**(파티원 · 캠프 상자를 한 창에). Script Extender + MCM 필요, 아직 베타, 가방 안까지 보이는지는 확인 필요. 아이템을 추가하지 않는 UI 모드라 빼도 물건은 안 사라짐.

## 진행 기록

### 📍 현재 상황 (2026-09-27)

- 위치: **언더다크 · 마이코니드 군락**
- 완료: 노틸로이드 탈출 · 난민 구하기(고블린 캠프) · 할신 구출 · 노움 구출 · 아라벨라 구하기 · 악마 사냥 · 일리시드 포로 구출
- 미탐색: **비전의 탑**, **그림포지**
- 소지금 **66골드** (Wyll 소지) — 가장 큰 병목. 인벤토리 상단의 53은 야영 물자(캠프파이어 아이콘)

### ✅ 지금 할 일 체크리스트

1. ☐ Wyll 목걸이 → **절대자의 호부**
2. ✅ 게일 → **회복의 애뮬릿** 착용
3. ☐ 게일과 대화 → **실격자의 애뮬릿** 주기 (워터딥의 위저드 "!")
4. ☐ 게일 → **방패** (경갑은 선택. 평갑은 숙련 없음)
5. ☐ Wyll 가방의 **책 전부 판매** → 골드 확보
6. ☐ 아스타리온·섀도하트에게 남는 장신구 나눠주기
7. ☐ 100골드씩 모이면 **위더스 리스펙**: 게일 → 섀도하트 → 아스타리온
8. ☐ **5레벨** 달성 (비전의 탑 일대 탐험)

### 🗺️ 퀘스트 우선순위

| 순위 | 퀘스트 | 구분 | 할 일 |
|---|---|---|---|
| 1 | 워터딥의 위저드 ❗ | 동료(게일) | 마법 물품 주기. 방치하면 호감도 하락·이탈 위험 |
| 2 | 오멜룸의 기생체 검사를 돕기 ❗ | 주요 | 마이코니드 군락 오멜룸과 대화 |
| ✅ | ~~버섯 채집꾼을 찾아서~~ (2026-10-16 완료) | 언더다크 | 비전의 탑 근처 베일런. 폭발 버섯 주의. 탑 탐험으로 5레벨 |
| 4 | 드웨가 침입자 쓰러뜨리기 ❗ | 언더다크 | 셀루네 전초성 선착장 → 그림포지, 니어 처치 · 툴라 해독 |
| 5 | 글럿 회합의 원수 갚기 ❗ | 언더다크 | **실행 비추천** (군락 전체와 적대) |
| 6 | 사라진 화물 찾기 | 지상 | 동굴 생존자 |
| 7 | 기스양키 양성소를 찾아서 | 주요(라에젤) | 떠오르는 길 기스양키 정찰대 → 산길 |
| 8 | 드루이드 할신 구출하기 | 주요 | 할신 관련 후속 |
| 9 | 밤의 노래를 찾아서 ❗ | 2막 진입 | **위 퀘스트들을 끝낸 뒤** 진행 |
| — | 타오르는 친구(카를라크) | 동료 | 1막 곳곳의 **지옥철** 모아두기 |

### Q1. 당장 금화를 구하는 방법 (2026-09-27)

인벤토리 상단 숫자 읽는 법: **캠프파이어 아이콘 = 야영 물자(53)**, **기둥 모양 아이콘 = 금화(66, Wyll 소지)**. 금화는 캐릭터마다 따로 들고 다녀요.

**1. 책 팔기 (가장 빠름)**
- Wyll 가방의 책 20권 정도를 마이코니드 군락 상인 **블러그**, **데리스**에게 판매.
- **주황색 테두리 아이템은 팔지 말 것** — 퀘스트·이야기 아이템.

**2. 잡동사니 · 남는 무기 팔기**
- 쓰지 않는 무기, 방어구, 은식기·술병 같은 잡템.
- 음식은 **팔지 말 것** — 긴 휴식에 야영 물자로 쓰여요.
- 두루마리는 게일이 배울 수 있는 것만 남기고 나머지는 팔아도 됨.

**3. 거래는 Wyll로**
- 매력이 가장 높아 판매가가 가장 좋아요. 파는 캐릭터를 Wyll로 바꾸고 거래.
- 상인도 금화가 한정돼 있어요. 상인 금화가 바닥나면 금화 대신 **물건으로 교환**(물약, 화살 등).

**4. 탐험하며 줍기**
- 언더다크 곳곳의 상자·시체, 특히 **비전의 탑**과 **셀루네 전초성**에 금화와 팔 물건이 많아요.
- 아스타리온으로 잠긴 상자를 전부 따기.

**목표 금액**
- 게일 리스펙 100골드 → 책만 팔아도 충분히 가능.
- 3명 모두 리스펙하려면 300골드 이상 → 비전의 탑 탐험 후.

### Q2. 골드 없이 게일 방어도 올리기 (2026-09-28)

**1순위: 마법사 갑옷(Mage Armor) 주문** — 돈 0원
- 게일 주문서에 **마법사 갑옷**이 있는지 확인. 있으면 전투 전에 걸기(긴 휴식까지 유지, 1레벨 슬롯).
- 방어도 11 → **14**. 방패까지 들면 **16**. 가죽 갑옷보다 좋아요.
- 갑옷을 입고 있으면 적용 안 됨. 게일은 로브 그대로.

**2순위: 가방·야영지 보관함 뒤지기**
- 인벤토리 검색창에 "갑옷" 입력. 고블린·도적에게서 주운 **가죽 / 누빔 / 징박은 가죽 갑옷**, **방패**가 있을 수 있어요.
- 게일은 인간 종족 특성 **민병대** 덕분에 경갑과 방패 숙련이 있어요.
- 아스타리온의 갑옷은 벗기지 말 것.

**3순위: 물물교환**
- 금화가 0이어도 거래 가능. 블러그·데리스 거래창에서 **책을 넘기고 갑옷·방패를 가져오면** 값이 상쇄돼요.
- 거래는 매력이 높은 Wyll로.

### Q3. 게일 점검 — 129골드 확보 (2026-09-28)

**완료**
- ✅ 회복의 애뮬릿 착용, 치유의 단어 · 다중 치유의 단어가 단축바에 추가됨
- ✅ 금화 129 (게일 소지)

**남은 것**
- 방어도 여전히 **11** → **방패**부터 (Q4 참고).
- **실격자의 애뮬릿**이 아직 가방에 있음 → 게일과 대화해서 건네기(워터딥의 위저드 "!").
- **야영 물자 13** → 긴 휴식 1회에 40 필요. 음식은 팔지 말고 줍기, 모자라면 상인에게서 음식 구매.

**금화 사용 순서**
1. 게일 갑옷 · 방패 구매
2. 남은 금화 + 책 판매로 100 모으기 → 위더스에서 게일 리스펙

### Q4. 데리스의 갑옷이 비싸요 (2026-09-28)

데리스가 파는 **생가죽 갑옷+1 (231골드)** 은 사지 말 것.
- **평갑(중갑)** 이라 게일은 **숙련이 없어요** (툴팁의 주황색 "평갑에 숙련되지 않음"). 입으면 주문을 못 쓰고 명중도 떨어져요.
- 게일이 입을 수 있는 건 **경갑**(누빔 · 가죽 · 징박은 가죽)과 **방패**뿐.

**가성비 계산 (게일 민첩 13 = +1)**

| 장비 | 방어도 | 비고 |
|---|---|---|
| 지금 로브 | 11 | |
| 가죽 갑옷 | 12 | +1밖에 안 오름 |
| 징박은 가죽 갑옷 | 13 | 비쌈 |
| **로브 + 방패** | **13** | 가장 쌈 |
| **마법사 갑옷 + 방패** | **16** | 최선 |

**결론**
1. **방패만 사기.** 상인 목록에서 "방패"를 찾거나, 동료 가방·야영지 보관함 확인.
2. 게일이 **마법사 갑옷** 주문을 알면 전투 전에 걸기. 갑옷은 필요 없음.
3. 비싼 건 금화 대신 **책을 거래창에 올려서** 값을 맞추기. 거래는 Wyll로.

### Q5. 방패를 상점 말고 구하는 곳 (2026-09-28)

**1. 이미 가진 것부터 (0골드)**
- 파티 4명 가방 + **야영지 보관함**에서 "방패" 검색.
- 야영지의 **라에젤 · 카를라크** 가방도 확인.

**2. 다녀온 곳의 시체 다시 뒤지기**
- **고블린 캠프(폐허가 된 성소)**: 고블린 전사들이 **나무 방패**를 많이 들고 있어요. 시체는 사라지지 않으니 순간 이동진으로 가서 줍기.
- 떠오르는 길 · 황폐한 마을의 적 시체도 마찬가지.

**3. 앞으로 얻을 곳**
- **그림포지 아다만틴 대장간**: 미스랄 광석 + 틀로 **아다만틴 방패**를 만들 수 있어요(갑옷 대신 선택). 게일이 들 수 있는 1막 최고급 방패.

**4. 장비 없이 방어도 올리는 주문**
- 게일 **방패(Shield)** 주문: 맞기 직전 반응으로 방어도 +5. 주문서에 있으면 준비해 두기.
- 섀도하트 **신앙의 방패**: 동료 한 명 방어도 +2 (집중 주문).
- 게일 **마법사 갑옷**: 로브 대신 방어도 14.

### Q6. 야영지 점검 — 방패 없음 (2026-09-28)

- 야영지 보관함 · 라에젤 · 윌(동료) · 카를라크 가방에 **방패 없음**.
- 보관함에 **갑옷 3벌**(붉은 갈색 조끼, 회색 사슬 셔츠, 파란 천 갑옷)이 있음 → 툴팁에 **"경갑"** 이라고 적힌 것만 게일이 입을 수 있음. 사슬 셔츠는 평갑이라 불가.
- 라에젤 가방에 **반지 1개**가 그냥 들어 있음 → 효과 확인 후 파티원에게 착용.
- 확인 결과: 붉은 갈색 조끼 = **가죽 갑옷(경갑, 방어도 11)** → 게일 착용 시 방어도 12. 단, **마법사의 갑옷(14)이 더 좋아서 입히지 않음** (Q7).
- 마법사 갑옷 주문을 쓸 땐 갑옷을 벗어야 함(마법사 갑옷 쪽이 14로 더 높음).
- 다음 수단: 고블린 캠프 시체에서 나무 방패 줍기 → 가죽 갑옷 + 방패 = **14**.

### Q7. 게일은 마법사의 갑옷을 이미 알고 있음 (2026-09-28)

- 단축바 아래 줄의 **노란 방패 아이콘 = 마법사의 갑옷** (1레벨 방호술, 긴 휴식까지 유지).
- 방어도 = 13 + 민첩(+1) = **14**. 가죽 갑옷(12)보다 높음.
- **조건: 갑옷을 입고 있으면 안 됨** → 가죽 갑옷은 입히지 말고 로브 그대로.
- 사용법: **긴 휴식 직후, 전투 밖에서 한 번** 걸어두기. 1레벨 슬롯 하나로 하루 종일 유지.
- 나중에 방패를 구하면 **16**.

### Q8. 불레트 처치 후 다음 행선지 (2026-10-16)

현재 위치: 언더다크 **공포의 골짜기(Dread Hollow)** — 가운데 수수르 나무를 둘러싼 고리 모양 지역.

**근처에서 할 일 (추천 순서)**
1. **버섯 채집꾼 구출 (베일런)** — 골짜기 북동쪽 **비버뱅 동굴**, 폭발 버섯 한가운데에 갇힘.
   - 버섯을 밟거나 불을 붙이면 폭발. 뛰어들지 말 것.
   - 베일런의 **안개 걸음 두루마리**를 그에게 던져 주면 순간이동으로 탈출. 마법사의 손으로 전달해도 됨.
   - 보상: 투명화 두루마리, 데리스 퀘스트 완료. 동굴 안쪽 바위 위에 **탐험가의 반지**.
2. **수수르 나무 껍질** — 나뭇가지에서 획득(마스터워크 무기 퀘스트 재료). 나무 근처에선 **주문 사용 불가**.
3. **남쪽 전망대** — 비전의 탑이 보이는 곳. 무덤의 **개 목걸이**. 가을 크로커스를 올리면 게일·카를라크·윌 호감도 상승.
4. **서쪽 동굴 필로(미친 드로우 위저드) + 훅 호러** — 보자마자 적대. 노트가 **아다만틴 대장간** 퀘스트와 연결. 5레벨 이후 추천.
5. **비전의 탑** 탐험 → 5레벨, 전리품.

**주의**: 수수르 나무 근처 전투에서는 게일·섀도하트가 주문을 못 써요. 싸움은 나무에서 떨어져서.

### Q9. 베일런의 가방을 들어가지 않고 줍는 법 (2026-10-16)

**마법사의 손(Mage Hand)** 을 쓰면 됨. 손은 비버뱅 버섯을 지나가도 **포자를 터뜨리지 않아요**.
- **아스타리온**(비전 괴도)은 마법사의 손을 무조건 갖고 있음. 게일에게 있으면 게일도 가능.

순서
1. 버섯 밭 가장자리에서 아스타리온으로 **마법사의 손 소환**.
2. 소환된 손을 선택해 **베일런의 가방 쪽으로 이동** (버섯 위를 지나가도 괜찮음).
3. 손의 **던지기**로 가방을 **베일런에게 던지기** → 베일런이 안의 안개 걸음 두루마리로 순간이동해서 탈출.
   - 파티 쪽으로 던져서 받은 다음, 두루마리만 베일런에게 던져줘도 됨.

✅ **2026-10-16 구출 완료.** 동굴 안쪽 **탐험가의 반지(좌표 X: -12, Y: -50, 돌 받침대 위)** · **공작송이(귀족줄기, Noblestalk · X: -6, Y: -66) ✅ 획득** 챙기기 — 횃불을 먼저 끄면 비버뱅이 터져도 안 부서짐. 마법사의 손으로 옮길 땐 던지지 말고 끌어다 놓기. 용도: 섀도하트(설득 시 동료 퀘스트), 베일런(기억 회복), 툴라 해독 중 택1 → 다음은 비전의 탑.

예비책: 떨어진 **횃불을 먼저 주워서/꺼서** 불이 옮지 않게 하고, 베일런을 치유해 두면 폭발이 나도 버틸 가능성이 높아요.

### Q10. 오멜룸 퀘스트 — 비전의 탑 가는 법 (2026-10-24)

오멜룸의 기생체 검사 재료(**광기의 혀**, **팀마스크 포자**)는 **비전의 탑** 3층에 있어요.

**위치**: 언더다크 **남서쪽**. 공포의 골짜기 남쪽 전망대에서 보이는 탑.

**가는 길 (둘 중 하나)**
1. 순간 이동진 **언더다크 - 해변** → 바로 옆 **노후한 마을** → 마을 남동쪽 **작은 협곡을 점프**로 건너기. (⚠️ "황폐한 마을"은 지상 마을이라 다른 곳)
2. 지상 **에델 아줌마 집 지하의 요정 고리**를 타면 탑 입구로 바로.

**들어가기**
- 정문은 잠김 → 바로 **남쪽 열린 창문으로 점프**.
- 입구에 **비전 포탑 4개**. 체력은 낮지만 **쓰러뜨려도 다시 살아나고** 한 턴에 여러 번 쏨. 체력을 두 번 깎아야 잠시 꺼짐.
  - **추천: 싸우지 말고 우회** → 파란 버섯 길로 지하로 내려가 **엔진에 수서꽃** 넣기 = 포탑 **영구 정지**.
  - 싸운다면: 파티 전원을 사거리에 넣지 말고, 한 대씩 집중. 게일 **마법 화살**(무조건 명중) · Wyll 망치.

**엘리베이터 켜기**
1. 남쪽 문 → 발코니 → 동쪽 **파란 버섯**으로 점프 → 3층 발코니 → 아래 파란 버섯으로 지면까지 (높으면 안개 걸음).
2. 탑 뒤 정원에서 **수수르 꽃** 줍기.
3. 2층 발전기 옆 계단으로 내려가 **엔진에 수수르 꽃** 넣기 → 엘리베이터 작동 + 포탑 꺼짐.

✅ 2026-10-25 엔진 가동 → 엘리베이터 작동, 포탑 정지.

**재료 (3층, 엘리베이터로)**
- 팀마스크 포자: 북서쪽 책장
- 광기의 혀: 남동쪽 커다란 주황 버섯 밑

### Q11. 야영 물자 부족 — 긴 휴식이 반쪽짜리 (2026-10-24)

긴 휴식 1회에 **야영 물자 40**이 필요. 모자라면 **부분 휴식**이 되어 체력·주문 슬롯이 다 안 채워짐.

**물자 채우는 법**
1. **가방의 음식을 야영지로 보내기** — 음식 우클릭 → "야영지로 보내기". 가방에 들고만 있으면 숫자에 안 잡힐 수 있음. Wyll 가방에 빵·사과·생선·소시지가 많음.
2. **언더다크 버섯 줍기** — 길가 식용 버섯도 야영 물자. Alt로 보면서 주워 다니기.
3. **상인에게 음식 사기** — 마이코니드 군락 상인. 음식은 싸고 무게 대비 물자 효율이 좋은 걸로.

**물자를 아끼는 법**
- **짧은 휴식**(긴 휴식 사이 2회) 먼저: 체력 절반 회복, **게일의 비전 회복**으로 주문 슬롯 일부 복구.
- 치유 물약 · 섀도하트 치유 주문으로 메꾸고 긴 휴식은 주문 슬롯이 바닥났을 때만.

### Q12. 팔라 알루베 vs 파멸의 망치 (2026-10-24)

| | 팔라 알루베 (희귀 장검) | 파멸의 망치 (고급 대형 망치, 착용 중) |
|---|---|---|
| 피해 (Wyll) | 양손 1d10+5 · 한손 1d8+5 | 2d6+4 |
| 특징 | 마법 +1, **선율**(아군 명중 보조), **다용도** = 한손+방패 가능 | 공포(회복 불가), **집요함**(빗나가도 4 피해) |

- **Wyll은 망치 유지.** 양손 피해는 비슷하고, 빗나가도 4 피해가 들어가는 집요함이 더 안정적.
- **팔라 알루베는 섀도하트에게.** 하이 하프엘프라 장검 숙련 있음 → 방패와 같이 들고 지금 무기보다 명중·피해 +1, 선율로 파티 보조.
- 나중에 Wyll이 방패를 구하면 "팔라 알루베 + 방패"로 방어도 18 탱커 운용도 가능.

### Q13. 노후한 마을 드웨가 매복에서 계속 전멸 (2026-10-25)

✅ **2026-10-25 처치 완료** (수서꽃을 치운 뒤 승리).

상대: **게크 콜의 드웨가 분대** (투명 상태로 숨어 있다가 매복). 적은 5레벨, 우리는 4레벨 + 부분 휴식 상태라 불리.

**1. 싸우지 않기 (가장 추천)**
- 대화로 시작됨 → **Wyll(매력 최고)로 설득**. 성공하면 전투 없이 지나가고 "사라진 장화 찾기" 퀘스트로 이어짐.
- 대화 전에 **빠른 저장(F5)** → 주사위 실패하면 불러오기.
- 파티에 딥노움이 있으면 협상 불가(현재 파티는 해당 없음).

**2. 싸워야 한다면 준비**
- **긴 휴식을 제대로**(야영 물자 40, Q11) 하고 들어가기. 반쪽 휴식 상태로는 무리.
- 가능하면 **비전의 탑에서 5레벨** 먼저.
- 전투 직전 버프: 게일 **마법사의 갑옷**, Wyll **지원(절대자의 호부)**, 섀도하트 **축복 / 신앙의 방패**.

**3. 전투 요령**
- 마을이 **절벽 · 물가 투성이** → 드웨가를 **밀치기**로 떨어뜨리면 한 방. Wyll 밀치기, 게일 **천둥파**.
- 투명한 적은 공격하면 모습이 드러남 → 드러난 적에게 집중 공격.
- 게일은 **높은 곳 · 뒤쪽**, 섀도하트는 **영혼 수호자**(5레벨부터)로 근접 정리.
- 수적으로 밀리면 **좁은 길목**으로 물러나 한 명씩 상대.

**4. 그래도 힘들면**
- 설정 → 난이도를 **탐험가**로 잠깐 내렸다가 이 전투 후 되돌려도 됨.

### Q14. 파티 전원 "수서꽃 항마법장" — 주문 봉인 (2026-10-25)

**원인**: 누군가 가방에 **수서꽃**(수서나무 꽃)을 들고 있음. 들고 있는 사람과 **주변 아군까지** 주문을 못 씀.
→ Q13 매복 전투에서 계속 진 진짜 이유일 가능성이 큼. 게일 · 섀도하트가 주문을 하나도 못 쓰는 상태였음.

**해결**
1. 인벤토리 검색창에 **"수서"** 입력 → 누가 들고 있는지 찾기.
2. 우클릭 → **야영지로 보내기**. 야영지 **여행용 궤짝**에 두면 시들지 않고 보관됨.
3. 상태 아이콘이 사라졌는지 확인 후 전투.
- 비전의 탑 엔진에 넣을 때만 다시 꺼내 오기. 꽃은 언더다크 밖에선 시듦(야영지 궤짝은 예외).

**응용**: 적 주문시전자 근처에 던져 두면 적의 주문도 봉인 가능.

### Q15. 샤 신전 들어가는 법 (2026-10-25)

⚠️ **정정 (2026-10-25)**: 퀘스트 "밤의 노래를 찾아서"의 **샤 신전 = 2막 지역**. 일지에 "달오름 탑 근처 어딘가의 지하"라고 나옴 → 2막 **그림자 저주받은 땅**의 달오름 탑 근처 지하(샤의 시련). **1막에서는 갈 수 없음.** 1막을 다 끝내고 2막에 들어간 뒤 진행.

아래는 1막 그림포지에 있는 **다른** 샤 관련 장소(고대 신전) 정보 — 미스릴 광석 때문에 들를 가치 있음.

**가는 법**
- 그림포지 남쪽 **발굴지**에 **훼손된 샤 석상**(X: -614, Y: 314)이 있음.
- 방법 1: 움직이는 갑옷이 있는 **용암 지대** 근처로 **한 명만 조심해서 내려가** 틈새를 점프 → 신전 진입.
- 방법 2: **니어를 처치한 뒤**, 발굴지 독가스 뒤쪽의 **커다란 잠긴 문**이 열림 → 신전으로 바로.

**안에 있는 것**
- 검은 갑옷 해골들(샤 숭배자 — 역사 판정 DC 10).
- **거대한 미스릴 광맥** → 부수면 **미스릴 광석** = 아다만틴 대장간 재료. 아다만틴 갑옷의 핵심 재료라 꼭 챙기기.
- 그 외엔 막다른 곳.

### Q16. "진행하기 전에 다른 일을 마무리하십시오!" 경고 (2026-10-25)

**1막 → 2막(그림자 저주받은 땅)으로 넘어가는 문**. 넘어가면 **1막 지역(지상 · 언더다크)으로 돌아올 수 없음**. → **"아니요"**.

넘어가기 전에 끝낼 것
- 오멜룸 기생체 검사(비전의 탑), 니어 처치 · 노움 구출, 툴라 해독
- 그림포지 미스릴 → 아다만틴 대장간 갑옷
- 지상: 사라진 화물(생존자), 기스양키 양성소(라에젤), 동료 대화 · 야영 이벤트
- 레벨 **5 이상** (경고 문구 = 지금 레벨로는 2막이 어렵다는 뜻)

### Q17. 니어 위치 (절망의 용광로 = 그림포지) (2026-10-25)

- 한글판 지명: **절망의 용광로** = 그림포지.
- 니어는 드웨가 발굴지 끝, **무너진 돌무더기 뒤**에 갇혀 있음. 퀘스트 일지 → "드웨가 침입자 쓰러뜨리기" → **지도에서 보기**로 표시.
- 돌무더기 앞에서 **드웨가 하사관 스린**이 노움 노예들에게 땅을 파게 하고 있음. 다가가면 니어가 올챙이로 말을 걸어옴.

**돌무더기 뚫기**
- 아래층 "명상의 방"에 숨은 노움 **필로민**(잠긴 문 따고 진입)과 거래 → **룬화약 병** → 노움들에게 주면 폭파.
- 또는 드웨가 **브리스바**를 설득해 반란: 진영의 **감시의 눈**을 먼저 없애 달라고 함 → 이후 니어를 같이 처치하고 돈을 나눔.

**주의**
- Wyll은 팔라딘: **니어 편을 들거나 니어가 노예를 죽이게 두면 맹세 위반**.
- 니어 방 주변에 **독가스 분출구**.

### Q18. 기스양키 정찰대 — 꼭 싸워야 하나? (2026-10-25)

**안 싸워도 됨.** 조건이 맞으면 대화로 통과.

**A. 라에젤에게 맡기기 (가장 쉬움)**
1. 라에젤을 파티에 넣고 가면 라에젤이 먼저 달려가 대화가 시작됨.
2. **"라에젤에게 고개를 끄덕인다. 해 봐."** 류 선택 → 라에젤이 대신 말함 (라에젤 호감 +10).
3. **설득 DC 10**으로 라에젤에게 "맞춰 줘"라고 입모양 신호.
4. 배경에서 **기만 판정**(말하는 캐릭터 매력 기준)이 자동으로 굴러감 → 성공하면 보스가 라에젤에게 양성소로 오라 하고 떠남.

**B. 유물을 들키지 않는 법**
- **유물을 꺼내 보여주는 선택지는 절대 고르지 말 것** (전투 확정 + 라에젤·섀도하트 호감 −5).
- 보스가 **생각 탐지(독심술)** 를 걸어옴 → **비전 판정 DC 10**으로 눈치챈 뒤 **지혜 내성 DC 10**으로 저항. 마법사 계열은 지혜 판정 DC 5만.
  - Wyll은 팔라딘이라 지혜 내성 숙련이 있어 유리.
- 마지막 판정 하나만 통과하면 평화적으로 끝남. Wyll은 **맹세(선조의 맹세) 설득 DC 15** 선택지 사용 가능.

- 대화 전 **F5 저장** 필수. 실패하면 불러오기.

**실패하면**: 5레벨 전사 3 + 6레벨 지휘관 → 1막 최고 난도급. 지금 레벨로는 매우 위험. 싸워야 하면 성문 위 높은 곳에서 원거리로.
- 정찰대를 쓰러뜨려도 이후 기스양키 양성소 진행엔 지장 없음. 이기면 기스양키 무기 + 석판(라에젤이 해독 → 양성소 위치).

### Q19. 인벤토리 정리 — 가방 모드 충돌과 아이템 증발 (2026-10-26)

- 가방 모드 3개(BagsBagsBags · Reforged · Autosort Containers)가 동시에 켜져 있어 같은 물건을 서로 끌어감 → **Autosort Containers 제거**.
- 원조 BagsBagsBags를 끄면 가방에서 꺼내 옮긴 물건까지 사라짐(이전 세이브로 복구) → **원조 + Reforged 둘 다 유지**하기로.
- 같은 가방이 2개씩 생기는 건 정상. 한 세트만 몸에 들고 짝꿍은 여행용 궤짝에. 이름은 위 **가방 한영 대조표** 참고.

### Q20. 가방이 무거울 때 정리법 (2026-10-26)

**팔 곳 (언더다크)**: 순간 이동진 **마이코니드 군락** → 데리스 · 블러그. 그림포지(절망의 용광로)에도 상인 여럿.
**바로 줄이는 법**
- 당장 안 쓰는 건 우클릭 → **야영지로 보내기** (야영지 궤짝은 무게 제한 없음). 단, 음식은 보내면 야영 물자로 쓰임.
- 팔 물건은 우클릭 → **상품으로 표시**(Wares) → 상인 거래창에서 한 번에 팔기.
- 거래는 **Wyll**(매력 최고)로, 무거운 짐은 **Wyll·라에젤**(근력 18) 쪽으로.
**팔아도 되는 것**: 회색(일반) 무기 · 갑옷, 접시 · 술병 · 촛대 같은 잡동사니, 읽은 책.
**팔지 말 것**: **주황 테두리(이야기 아이템)**, 공작송이, 지옥철, 미스릴 광석, 두루마리 · 물약.

### Q21. 장밋빛 아침 수도원 — 잠긴 돌벽과 스테인드글라스 퍼즐 (2026-10-27)

**상황**: 수도원 2층 스테인드글라스 방(X:75 Y:75 부근)의 **잠긴 돌벽**. 점프·순간이동 시 "공간이 부족합니다 / 경로가 가로막혔습니다" → 환영이 아니라 진짜 벽.
**해결**: 방의 제단 4개에 의식용 무기를 올리면 장검과 망치 사이 벽이 열림. ✅ **2026-10-27 완료** (무기 4개 모두 배치).

| 제단 (새벽주인) | 무기 | 구하는 곳 |
|---|---|---|
| 처음부터 놓여 있음 | 의식용 장검 | 파란 불빛 두 개 제단 |
| **시드** (북동쪽) | 의식용 전투망치 | 수도원 **지붕 독수리 둥지** |
| **바세이드** | 의식용 전투도끼 | 2층 옛 숙소(X:105 Y:45), 수호자 처치 |
| **스톡홀드** (남동쪽) | 녹슨 메이스 (대체 가능) | 1층 X:85~87 Y:32 바닥, 또는 남동쪽 스톡홀드 무덤을 **삽**으로 파기 |

- **지붕 가는 길**: 그렘리슈카 방 → 판자로 막힌 출입구 부수기 → 밖의 **뒤엉킨 뿌리** 타고 오르기.
- **독수리**: 동물 조련 DC 18(또는 동물과 대화 + 설득)로 중립 유지, 은신으로 몰래 줍기, 또는 전투. 큰 독수리가 **지붕 밖으로 밀어내니** 가장자리 피하기.
- 진짜 의식용 메이스는 1층 **술 취한 코볼트**가 갖고 있음. 퍼즐엔 녹슨 메이스로 충분.
- 잘못 올려도 무기는 안 사라짐 — 제단 클릭하면 보관함처럼 열려서 다시 꺼낼 수 있음. 인벤토리 검색창에 `의식` 입력하면 의식용 무기만 보임.
- 자물쇠 따기로도 열 수 있지만 난이도가 매우 높음.
- 퍼즐이 끝나면 무기는 다시 가져가도 됨(성능 평범 → 팔거나 놔두기).

**다음**: 벽 속 주머니에서 **새벽주인의 문장** 챙기기 → 계단 아래 **태양 문양 문** → 비밀 방의 방어막 해제 → 서쪽 단상의 **라센더의 피**(전설 메이스).
⚠️ 문장 없이 라센더의 피를 집으면 수도원 붕괴 장치 작동 → **4턴 안에 탈출**.

### Q22. 수도원 정문이 잠겨 있을 때 들어가는 법 (2026-10-27)

정문 "장밋빛 아침 수도원 문"(마법이 부여된 보안)은 열쇠 · 자물쇠 따기로 안 열려요. **옆으로 들어가서 안쪽에서 정문을 열면** 돼요.
- **깨진 창문 (추천)**: 정문을 바라보고 **왼쪽 깨진 창문 두 개** → **점프**로 진입. 안에는 술 취해 자는 코볼트들. 은신해서 지나가거나 쏟아진 술에 불을 붙여 처리(파티원 거리 두기).
- **2층 판자 구멍**: 웨이포인트 근처 **덩굴 → 절벽** → 판자를 일반 공격으로 부수기. 안에 **그레미시카** 무리 → Q23.
- 진입 전 **F5 저장**.

### Q23. 그레미시카 공략 (2026-10-27)

체력 16 · 방어도 13 · 1레벨(균형). 약하지만 **마법 알레르기**가 있어요.
- 근처에서 **주문 · 소마법을 쓰면 "불안정"** → 다음 턴 시작에 무작위 효과: **분열(2마리로)**, 표범 변신, 거울 분신 + 거대화 + 신속, 역장 폭발(멍해짐), 얼음 바닥. 여러 마리가 연쇄로 터질 수 있음.
- **회피(Evasion)** 보유 → 화염구 같은 범위 주문은 효과가 거의 없음.

**공략**
1. **무기 공격만**: 윌의 망치, 근접 동료의 무기, 아스타리온의 활. 게일도 이번엔 석궁 · 단검.
2. **버프는 미리**: 축복 등은 그레미시카가 안 보이는 곳에서 걸고 진입.
3. **절벽에서 받아치기**: 판자 구멍 밖에 서 있으면 뛰어와서 모임 → 입구에서 한 마리씩.
4. 불안정 표시가 뜬 놈은 **그 턴 안에 먼저 처치** → 효과 발동 전에 막기.
- 싸우기 싫으면 **깨진 창문** 쪽으로(Q22).

### ⚔️ 장비 업그레이드 목표

- **그림포지 아다만틴 대장간**: 미스랄 광석 + 틀 → **아다만틴 판금(Wyll)** 또는 **아다만틴 비늘 갑옷(섀도하트)**. 1막 최고 방어구.
- 골드 목표: 리스펙 300 + 주문서 학습비.

## 참고 자료

- [Gremishka - bg3.wiki](https://bg3.wiki/wiki/Gremishka)
- [Unstable (condition) - bg3.wiki](https://bg3.wiki/wiki/Unstable_(condition))
- [How to Enter the Rosymorn Monastery - Prima Games](https://primagames.com/tips/baldurs-gate-3-how-to-enter-the-rosymorn-monastery-in-bg3)
- [Inventory Expanded - Nexus Mods](https://www.nexusmods.com/baldursgate3/mods/22267)
- [Inventory Management Tips - Gamer Guides](https://gamerguides.com/baldurs-gate-3/guide/gameplay/basics/inventory-management-tips-in-baldurs-gate-3)
- [Bags Bags Bags - Nexus Mods](https://www.nexusmods.com/baldursgate3/mods/880)
- [Bags Bags Bags - REFORGED - Nexus Mods](https://www.nexusmods.com/baldursgate3/mods/5422)
- 가방 한글·영문 이름: 설치된 BagsBagsBagsReforged.pak · BagsBagsBagsReforged-KR.pak 번역 파일에서 직접 추출 (2026-10-26)
- [Dread Hollow - bg3.wiki](https://bg3.wiki/wiki/Dread_Hollow)
- [Baelen Bonecloak - bg3.wiki](https://bg3.wiki/wiki/Baelen_Bonecloak)
- [Noblestalk - bg3.wiki](https://bg3.wiki/wiki/Noblestalk)
- [Find the Githyanki Crèche - bg3.wiki](https://bg3.wiki/wiki/Find_the_Githyanki_Cr%C3%A8che)
- [Risen Road - EIP Gaming](https://eip.gg/bg3/guides/risen-road/)
- [Grymforge - bg3.wiki](https://bg3.wiki/wiki/Grymforge)
- [Grymforge - Fextralife](https://baldursgate3.wiki.fextralife.com/Grymforge)
- [Sussur Bloom - bg3.wiki](https://bg3.wiki/wiki/Sussur_Bloom)
- [Decrepit Village - bg3.wiki](https://bg3.wiki/wiki/Decrepit_Village)
- [Arcane Tower guide - PC Gamer](https://www.pcgamer.com/baldurs-gate-3-arcane-tower-omeelum-underdark/)

- [Rosymorn Monastery - bg3.wiki](https://bg3.wiki/wiki/Monastery)
- [Rosymorn Monastery puzzle - PC Gamer](https://pcgamer.com/baldurs-gate-3-rosymorn-monastery-puzzle)
- [Dawnmaster's Crest - Prima Games](https://primagames.com/tips/baldurs-gate-3-how-to-get-the-dawnmasters-crest-in-bg3)
- [Ceremonial Weapon Locations - Dot Esports](https://dotesports.com/?p=997034)
- [Find the True Blood of Lathander - Nightly Gaming Binge](https://nightlygamingbinge.com/find-the-true-blood-of-lathander-baldurs-gate-iii/)
- [Rosymorn Monastery - Fextralife](https://baldursgate3.wiki.fextralife.com/ROSYMORN+MONASTERY)

- 2026-09-27 스크린샷 기반 파티 분석 (캐릭터 시트 · 퀘스트 일지 · 언더다크 지도)
