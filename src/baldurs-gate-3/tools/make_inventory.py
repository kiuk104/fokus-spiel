"""fokus_inventory.json (Script Extender 내보내기) → 위키용 인벤토리 목록 HTML 조각"""
import json, pickle, sys, html, collections, os, re
S = os.path.dirname(os.path.abspath(__file__))
inv = json.load(open(sys.argv[1], encoding='utf-8'))
date = sys.argv[2]; icon_dir = sys.argv[3]; out = sys.argv[4]
hist_path = sys.argv[5] if len(sys.argv) > 5 else None
party_out = sys.argv[6] if len(sys.argv) > 6 else None
books_out = sys.argv[7] if len(sys.argv) > 7 else None
BOOKS = pickle.load(open(os.path.join(S, 'books.pkl'), 'rb')) if os.path.exists(os.path.join(S, 'books.pkl')) else {}
en, kr = pickle.load(open(os.path.join(S, 'loca.pkl'), 'rb'))
mod = json.load(open(os.path.join(S, 'loca.json'), encoding='utf-8'))
en.update(mod['en']); kr.update(mod['kr'])
have_icon = {os.path.splitext(f)[0] for f in os.listdir(icon_dir)}
CATS = [('가방', ('OBJ_LIA_', 'OBJ_Bag_', 'OBJ_Backpack', 'OBJ_Keychain', 'OBJ_Chest', 'DOR_')),
        ('물약', ('OBJ_Potion', 'ALCH_Solution_Elixir', 'OBJ_Antitoxin', 'OBJ_Elixir')),
        ('두루마리', ('OBJ_Scroll_',)),
        ('화살', ('OBJ_Arrow',)),
        ('투척물', ('OBJ_GreaseBottle', 'OBJ_AcidBottle', 'OBJ_Bomb', 'OBJ_FireBottle', 'OBJ_Bag_BlackPowder', 'OBJ_Grenade', 'GRN_', 'OBJ_Smoke', 'OBJ_Frost', 'OBJ_Holy')),
        ('독·도포제', ('ALCH_Solution_Oil', 'OBJ_BasicPoison', 'OBJ_Poison', 'ALCH_Solution_Coating')),
        ('무기', ('WPN_',)),
        ('반지', ('ARM_Ring',)),
        ('목걸이', ('ARM_Amulet', 'ARM_KeepsakeLocket')),
        ('야영지 옷', ('ARM_Camp', 'ARM_Underwear')),
        ('방어구', ('ARM_',)),
        ('마법 장비', ('MAG_', 'UNI_', 'UND_', 'GOB_', 'GLO_')),
        ('책·쪽지', ('OBJ_Book', 'BOOK_', 'OBJ_Scroll', 'OBJ_Note', 'LOOT_Book')),
        ('열쇠', ('PUZ_Key', 'OBJ_Key')),
        ('염료', ('OBJ_Dye', 'DLC_OBJ_Dye')),
        ('음식·술', ('CONS_FOOD', 'CONS_GEN_Food', 'CONS_DRINK', 'CONS_Drink', 'CONS_GEN_Alcohol', 'CONS_Fungi', 'CONS_Food')),
        ('연금술 재료', ('ALCH_', 'CONS_Herbs', 'CONS_Mushrooms', 'OBJ_Crystal', 'LOOT_Underdark', 'OBJ_Myconid')),
        ('보석·귀중품', ('OBJ_Malachite', 'OBJ_Bloodstone', 'OBJ_Gem', 'LOOT_GEM', 'OBJ_GoldPile', 'OBJ_Agate', 'OBJ_Metalbar')),
        ('잡동사니', ('OBJ_Bottle', 'OBJ_Bucket', 'OBJ_Cauldron', 'OBJ_Bone', 'OBJ_Candle', 'OBJ_MilkCan', 'OBJ_Skull', 'OBJ_Demijohn', 'OBJ_Chalice', 'OBJ_InkPot', 'Cup_', 'OBJ_Cup', 'OBJ_Plate', 'OBJ_Barrel', 'OBJ_Crate', 'OBJ_Bowl', 'OBJ_Rag', 'OBJ_VolatileBladder', 'OBJ_MindflayerBulb')),
        ('도구', ('OBJ_Tool', 'OBJ_Kit', 'OBJ_Rope', 'OBJ_Bedroll'))]
def cat(st):
    st = st or ''
    for name, prefs in CATS:
        if st.startswith(prefs): return name
    return '기타'
def is_member(c):
    if c.get('kind') in ('party', 'campchest', 'member'): return True
    return any(x.get('classH') for x in (c.get('charStats') or {}).get('classes', []))
inv['chars'] = [c for c in inv['chars'] if is_member(c)]
SLOT = {'Helmet': '투구', 'Breast': '갑옷', 'Cloak': '망토', 'Melee Main Weapon': '근접 주무기', 'Melee Offhand Weapon': '근접 보조', 'Ranged Main Weapon': '원거리 무기', 'Ranged Offhand Weapon': '원거리 보조', 'Ring': '반지', 'Ring2': '반지', 'Boots': '장화', 'Gloves': '장갑', 'Amulet': '목걸이', 'MusicalInstrument': '악기'}
EQ = {}
for c in inv['chars']:
    for e in (c.get('charStats') or {}).get('equipped', []):
        if e.get('uuid'): EQ[e['uuid']] = SLOT.get(e.get('eqslot'), e.get('eqslot'))
BOOKLIST = []
ORDER = {c: i for i, (c, _) in enumerate(CATS)}; ORDER['기타'] = 99

KEEP, SELL, MAYBE = '🟢 보관', '🔴 팔기', '🟡 비교'
# 아이템별 판단 (stats ID 기준) — 파티: Wyll(팔라딘) · 게일(위저드) · 아스타리온(로그) · 라에젤(전사) · 섀도하트(클레릭)
OVR = {
 'MAG_Monk_Magic_Gloves': (SELL, '몽크 전용 — 파티에 몽크 없음'),
 'MAG_Monk_Fire_Gloves': (SELL, '몽크 전용 — 파티에 몽크 없음'),
 'MAG_BarbMonk_Defensive_Cloth': (MAYBE, '바바리안·몽크용 — 카를라크를 쓸 거면 보관, 아니면 비싸게 팔림'),
 'MAG_Thunder_ThunderClap_Quarterstaff': (SELL, '근접 지팡이 — 게일은 주문 위주라 쓸 일 적음'),
 'MAG_Bard_TempHP_Armor': (SELL, '바드용 — 파티에 바드 없음'),
 'UND_DuergarRaft_PestKillerAxe': (SELL, '평범한 대형 도끼'),
 'MAG_Mobility_MomentumOnCombatStart_Helmet': (KEEP, '전투 시작 시 이동력 — 누구나 좋음, 장착 추천'),
 'MAG_Healer_TempHPOnHeal_Boots': (KEEP, '치유하면 임시 생명력 — 섀도하트'),
 'UNI_ARM_OfArchery_Gloves': (KEEP, '원거리 명중 +2 — 아스타리온'),
 'GOB_Priest_Amulet': (KEEP, '지원 주문 — Wyll (목걸이 배분표)'),
 'GOB_Priest_Shield': (KEEP, '방패 — Wyll이 한손 무기 쓸 때 / 섀도하트'),
 'UND_MushroomHunger_RingOfExploration': (KEEP, '장착 추천'),
 'UNI_UND_RingOfMindShielding': (KEEP, '장착 추천'),
 'UND_Tower_AmuletDetectThoughts': (KEEP, '생각 탐지 — 대화에 유용'),
 'UND_Minotaur_BeltAmulet': (KEEP, '게일에게 먹이기 (개인 퀘스트)'),
 'MAG_Healer_HPRestoration_Amulet': (KEEP, '치유의 단어 — 게일'),
 'FOR_OgresForHire_HeadbandOfIntellect': (MAYBE, '오우거 퀘스트 물건 — 쓸 일 없으면 270골드에 팔기'),
 'FOR_SchoolOgres_Horn': (KEEP, '고용한 오우거 부르기'),
 'MAG_Violence_LowHP_Violence_Clothes': (MAYBE, '아스타리온 갑옷과 비교'),
 'PLA_WPN_SwordOfJustice': (MAYBE, '라에젤 지금 무기와 비교'),
 'UNI_DoomHammer': (MAYBE, 'Wyll 예전 주무기 — 지금 무기가 더 좋으면 팔기'),
 'UND_Wand_Fireballs_Crooked': (KEEP, '화염구 마법봉'),
 'UNI_MagicStaff_Part_Crystal': (KEEP, '지팡이 부품'),
 'GLO_SoulCoin': (KEEP, '나중에 쓰임'),
 'COL_BrainJar_Memory': (KEEP, '이야기 관련일 수 있음'),
 'OBJ_Myconid_Flesh': (KEEP, ''),
 'OBJ_Tool_Shovel': (KEEP, '무덤 파기'),
 'OBJ_Kit_TrapDisarm': (KEEP, '함정 해제'),
 'OBJ_GenericLootItem': (SELL, ''),
 'OBJ_Barrel_Filled_Oil': (SELL, '무거움'),
 'ARM_Instrument_Lute_B': (SELL, '악기'),
 'OBJ_Bedroll': (SELL, ''), 'OBJ_Rope': (SELL, ''),
 'ARM_KeepsakeLocket_A': (KEEP, '팔지 말 것 (목걸이 배분표)'),
 'ARM_Amulet': (KEEP, '로켓 · 목걸이 — 이야기 관련일 수 있음'),
 'CONS_DRINK_Water_Bottle': (KEEP, '야영 물자'),
 'WPN_LightCrossbow': (MAYBE, '섀도하트 원거리 무기가 없으면 주기'),
}
for k in ('ARM_HalfPlate', 'ARM_ChainMail', 'ARM_Splint', 'ARM_Plate', 'GTY_', 'ARM_Githyanki'):
    pass
HEAVY = ('HalfPlate', 'ChainMail', 'Splint', 'Plate_Body', 'Githyanki')
def verdict(x):
    st = x.get('stats') or ''; c = cat(st)
    if x.get('uuid') in EQ: return ('🛡️ 착용 중', EQ[x['uuid']])
    if st in OVR: return OVR[st]
    if st.startswith('ARM_') and any(h in st for h in HEAVY) and 'ChainShirt' not in st: return (MAYBE, '중갑 — Wyll·라에젤 지금 갑옷과 비교')
    if x.get('story'): return (KEEP, '이야기 아이템')
    if 'Rotten' in st: return (SELL, '썩은 음식')
    if c in ('가방', '물약', '두루마리', '화살', '투척물', '독·도포제', '연금술 재료', '열쇠', '염료', '음식·술', '야영지 옷'): return (KEEP, '')
    if c in ('잡동사니', '보석·귀중품'): return (SELL, '돈으로 바꾸기')
    if c == '책·쪽지': return (SELL, '읽은 뒤 팔기')
    if c in ('무기', '방어구', '반지', '목걸이', '마법 장비'):
        if (x.get('rarity') or 0) >= 1: return (MAYBE, '지금 장비와 비교')
        return (SELL, '평범한 장비')
    if c == '도구': return (KEEP, '')
    return (MAYBE, '')
SELL_LIST = []
RAR = {1: '#3f9d4a', 2: '#3a7bd5', 3: '#9b4dd6', 4: '#d39c3c'}
def names(x):
    k = x.get('name') or ''
    e = en.get(x.get('h') or '')
    if e is None:        # 원조 BagsBagsBags 처럼 한글 번역이 없는 모드 아이템
        return '', k
    return k, e
def img(x):
    ic = x.get('icon')
    col = RAR.get(x.get('rarity') or 0)
    st = 'width:32px;height:32px;vertical-align:middle;border-radius:4px;' + ('box-shadow:0 0 0 2px %s;' % col if col else '')
    if ic in have_icon:
        return '<img src="icons/items/%s.png" alt="" loading="lazy" width="32" height="32" style="%s">' % (html.escape(ic), st)
    return ''
def rows(items, where=''):
    g = collections.OrderedDict()
    for x in items or []:
        if 'err' in x: continue
        if x.get('items'): continue   # 가방은 따로 섹션으로
        key = (x.get('h'), x.get('stats'), x.get('name'), x.get('uuid') in EQ)
        if key not in g: g[key] = [x, 0]
        g[key][1] += x.get('amount') or 1
    lst = sorted(g.values(), key=lambda v: (ORDER[cat(v[0].get('stats'))], names(v[0])[0] or names(v[0])[1]))
    out = []
    for x, n in lst:
        k, e = names(x)
        badge = ' <span title="이야기 아이템" style="color:#c96a12">◆</span>' if x.get('story') else ''
        v, why = verdict(x)
        if x.get('book') and x['book'] in BOOKS:
            BOOKLIST.append((x, where)); badge += ' <a href="#book-%s" title="원문 · 번역 보기">📖</a>' % re.sub(r'[^A-Za-z0-9_-]', '', x['book'])
        if v == SELL and x.get('stats') != 'OBJ_GoldPile': SELL_LIST.append((x, n, where))
        if x.get('stats') == 'OBJ_GoldPile': v, why = '', ''
        out.append('<tr><td>%s</td><td>%s%s</td><td>%s</td><td style="text-align:right">%s</td><td>%s</td><td style="white-space:nowrap">%s</td><td style="opacity:.75">%s</td></tr>' % (
            img(x), html.escape(k) if k else '<span style="opacity:.6">(한글 없음)</span>', badge, html.escape(e or ''), n, cat(x.get('stats')), v, html.escape(why)))
    return out
def table(r):
    return ('<table><thead><tr><th></th><th>한글 이름</th><th>영문 이름</th><th>개수</th><th>종류</th><th>판정</th><th>이유</th></tr></thead><tbody>%s</tbody></table>' % ''.join(r))
def count(items):
    c = 0
    for x in items or []:
        if 'err' in x: continue
        if not x.get('items') and x.get('stats') != 'OBJ_GoldPile': c += x.get('amount') or 1
        c += count(x.get('items'))
    return c
def walk(items):
    for x in items or []:
        yield x
        yield from walk(x.get('items'))
parts = []
parts.append('### 📦 지금 들고 있는 아이템 (%s)\n' % date)
parts.append('게임 안에서 Script Extender로 뽑은 실제 목록이에요. **한글 이름 = 게임 화면 그대로**, 영문 이름은 같은 아이템의 공식 영문판 이름이에요. 테두리 색 = 희귀도(초록 고급 · 파랑 희귀 · 보라 매우 희귀 · 금색 전설), ◆ = 이야기 아이템. 개수는 같은 아이템을 합친 값이에요.\n')
parts.append('<span style="opacity:.75">원조 BagsBagsBags 가방은 한글 번역이 없어 영문으로만 나와요. 갱신하려면 게임 콘솔에서 <code>load(Ext.IO.LoadFile("fokus_inv.lua"))()</code> 실행 → "인벤토리 목록 갱신".</span>\n')
for c in inv['chars']:
    who = c.get('name') or '?'
    total = count(c.get('items'))
    body = []
    top = rows(c.get('items'), who + ' · 가방 밖')
    if top: body.append('<p><b>가방 밖</b></p>' + table(top))
    for x in sorted([x for x in c.get('items') or [] if x.get('items')], key=lambda x: names(x)[0] or names(x)[1]):
        k, e = names(x)
        label = (k + ' · ' + e) if k else e
        sub = rows(x.get('items'), who + ' · ' + label)
        nested = [y for y in x.get('items') if y.get('items')]
        for y in nested:
            sub += ['<tr><td colspan="7"><i>└ %s 안</i></td></tr>' % html.escape(names(y)[0] or names(y)[1])] + rows(y.get('items'), who + ' · ' + label)
        body.append('<p>%s <b>%s</b> <span style="opacity:.6">(%d)</span></p>' % (img(x), html.escape(label), count(x.get('items'))) + table(sub))
    gold = sum((x.get('amount') or 0) for x in walk(c.get('items')) if x.get('stats') == 'OBJ_GoldPile')
    parts.append('<details><summary><b>%s</b> — 아이템 %d개%s</summary>\n\n%s\n\n</details>\n' % (html.escape(who), total, (' · 금화 %d' % gold) if gold else '', '\n'.join(body)))
tot = sum((x.get('value') or 0) * n for x, n, w in SELL_LIST)
sell_rows = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td><td style="text-align:right">%d</td><td style="text-align:right">%d</td><td>%s</td></tr>' % (
    img(x), html.escape(names(x)[0] or names(x)[1]), html.escape(names(x)[1] or ''), n, (x.get('value') or 0) * n, html.escape(w))
    for x, n, w in sorted(SELL_LIST, key=lambda t: -((t[0].get('value') or 0) * t[1])))
summary = ('#### 🔴 팔 것 한눈에 — %d종 · 기본가 합계 약 %d골드\n\n'
  '상인 거래창에서 우클릭 → **판매 목록에 넣기**(Mark as Wares)로 모아 한 번에 파세요. 실제 판매가는 매력·상인 호감도에 따라 기본가보다 낮아요. 🟡 비교 항목은 지금 장착한 장비와 비교해 보고 결정하세요.\n\n'
  '<details><summary><b>팔 것 목록 펼치기</b> (비싼 순)</summary>\n\n<table><thead><tr><th></th><th>한글 이름</th><th>영문 이름</th><th>개수</th><th>기본가</th><th>어디에</th></tr></thead><tbody>%s</tbody></table>\n\n</details>\n') % (len(SELL_LIST), tot, sell_rows)
parts.insert(3, summary)
# ---- 판매·없어진 아이템 (이전 목록과 비교)
if hist_path:
    hist = json.load(open(hist_path, encoding='utf-8')) if os.path.exists(hist_path) else {'items': {}}
    H = hist['items']
    bb = {b.get('uuid'): b for b in inv.get('buyback') or [] if b.get('uuid')}
    cur = {}
    for c in inv['chars']:
        who = c.get('name') or '?'
        for x in walk(c.get('items')):
            if x.get('uuid') and not x.get('items') and x.get('stats') != 'OBJ_GoldPile': cur[x['uuid']] = (x, who)
    for u, (x, who) in cur.items():
        k, e = names(x)
        H[u] = {'ko': k, 'en': e, 'icon': x.get('icon'), 'value': x.get('value') or 0, 'amount': x.get('amount') or 1,
                'rarity': x.get('rarity') or 0, 'owner': who, 'verdict': verdict(x)[0], 'last': date,
                'first': H.get(u, {}).get('first', date), 'status': 'have'}
    for u, r in H.items():
        if r.get('status') == 'have' and u not in cur:
            if u in bb: r.update(status='sold', gone=date, trader=bb[u].get('trader'))
            elif r.get('verdict') == SELL: r.update(status='sold', gone=date)
            else: r.update(status='gone', gone=date)
    json.dump(hist, open(hist_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    gone = sorted([r for r in H.values() if r.get('status') in ('sold', 'gone')], key=lambda r: (r.get('gone', ''), -(r['value'] * r['amount'])), reverse=True)
    if gone:
        sold_total = sum(r['value'] * r['amount'] for r in gone if r['status'] == 'sold')
        grow = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td style="text-align:right">%d</td><td style="text-align:right">%d</td><td>%s</td><td>%s</td></tr>' % (
            r.get('gone', ''), img({'icon': r.get('icon'), 'rarity': r.get('rarity')}), html.escape(r['ko'] or ''), html.escape(r['en'] or ''), r['amount'], r['value'] * r['amount'],
            '💰 판매됨' + (' (%s)' % html.escape(r['trader']) if r.get('trader') else '') if r['status'] == 'sold' else '➖ 없어짐', html.escape(r.get('owner', ''))) for r in gone)
        parts.insert(4, ('#### 💰 판매한 아이템 · 없어진 아이템 — 판매 %d종 · 기본가 %d골드\n\n'
            '이전 목록에 있다가 사라진 아이템이에요. **💰 판매됨** = 🔴 팔 것이었거나 상인 되사기 목록에 있는 것, **➖ 없어짐** = 그 밖에 사용 · 버림 · 건네준 것.\n\n'
            '<details><summary><b>목록 펼치기</b> (최근 순)</summary>\n\n<table><thead><tr><th>날짜</th><th></th><th>한글 이름</th><th>영문 이름</th><th>개수</th><th>기본가</th><th>상태</th><th>원래 누구</th></tr></thead><tbody>%s</tbody></table>\n\n</details>\n')
            % (sum(1 for r in gone if r['status'] == 'sold'), sold_total, grow))
# ---- 책 원문 · 번역
def clean(t):
    t = re.sub(r'<LSTag[^>]*>(.*?)</LSTag>', r'\1', t or '', flags=re.S)
    t = re.sub(r'<br\s*/?>', '\n', t)
    t = re.sub(r'<(?!/?(i|b)>)[^>]+>', '', t)
    return html.escape(t).replace('&lt;i&gt;', '<i>').replace('&lt;/i&gt;', '</i>').replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>').replace('\n', '<br>')
if books_out:
    seen = collections.OrderedDict()
    for x, where in BOOKLIST:
        seen.setdefault(x['book'], [x, []])[1].append(where)
    bparts = ['### 📚 책 · 쪽지 — 영문 원문과 한글 번역 (%s)\n' % date,
              '지금 들고 있는 책 · 쪽지 %d종이에요. 게임 파일에서 공식 영문 원문과 한글 번역을 그대로 가져왔어요. 인벤토리 목록의 📖 를 누르면 여기로 와요.\n' % len(seen)]
    for bid, (x, wheres) in sorted(seen.items(), key=lambda t: names(t[1][0])[0] or ''):
        h = BOOKS[bid]; k, e = names(x)
        anchor = 'book-' + re.sub(r'[^A-Za-z0-9_-]', '', bid)
        story = ' ◆' if x.get('story') else ''
        bparts.append('<details id="%s"><summary>%s <b>%s</b>%s <span style="opacity:.65">· %s · %s</span></summary>\n\n'
            '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:10px 0 18px">'
            '<div><div style="font-size:12px;opacity:.6;margin-bottom:4px">한글</div><div style="line-height:1.75">%s</div></div>'
            '<div><div style="font-size:12px;opacity:.6;margin-bottom:4px">English</div><div style="line-height:1.65">%s</div></div></div>\n\n</details>\n' % (
            anchor, img(x), html.escape(k), story, html.escape(e or ''), html.escape(' / '.join(sorted(set(wheres)))), clean(kr.get(h)), clean(en.get(h))))
    open(books_out, 'w', encoding='utf-8').write('\n'.join(bparts))
# ---- 파티 현황판
if party_out:
    AB = ['근력', '민첩', '건강', '지능', '지혜', '매력']
    ROLE = {'Paladin': '탱커 겸 근접 딜러', 'Wizard': '원거리 광역 딜러', 'Rogue': '딜러 · 자물쇠/함정', 'Fighter': '근접 딜러', 'Cleric': '힐러 · 버프', 'Warlock': '원거리 딜러', 'Barbarian': '근접 탱커 · 딜러'}
    MAIN = {'Paladin': 0, 'Wizard': 3, 'Rogue': 1, 'Fighter': 0, 'Cleric': 4, 'Warlock': 5, 'Barbarian': 0}
    rowsP = []
    for c in inv['chars']:
        cs = c.get('charStats') or {}
        if not cs.get('classes'): continue
        cl = cs['classes'][0]; cname = cl.get('className')
        ko_cls = '%s · %s' % (kr.get(cl.get('classH'), cname), kr.get(cl.get('subH'), ''))
        a = (cs.get('abilities') or [])[1:7]
        mi = MAIN.get(cname)
        abil = ' · '.join(('<b>%s %d</b>' if i == mi else '%s %d') % (AB[i], v) for i, v in enumerate(a))
        eq = {e['eqslot']: e for e in cs.get('equipped', [])}
        wpn = ' / '.join(html.escape(eq[k]['name']) for k in ('Melee Main Weapon', 'Melee Offhand Weapon', 'Ranged Main Weapon') if k in eq) or '—'
        notes = []
        if mi is not None and len(a) > mi and a[mi] % 2 == 1 and (cs.get('level') or 0) >= 4: notes.append('⚠️ 주 능력치 %d(홀수) → 리스펙 추천' % a[mi])
        if 'Melee Main Weapon' not in eq and cname in ('Paladin', 'Fighter', 'Barbarian'): notes.append('🚨 근접 무기 없음')
        if 'Ranged Main Weapon' not in eq: notes.append('원거리 무기 없음')
        if (cs.get('ac') or 0) <= 12: notes.append('🚨 방어도 낮음')
        if not notes: notes.append('✅')
        where = '파티' if c.get('kind') in ('party', 'member') else '야영지'
        rowsP.append('| **%s** (%s) | %s | %s | %s | %s/%s | %s | %s | %s | %s |' % (
            c['name'], where, ko_cls, ROLE.get(cname, ''), cs.get('level'), cs.get('hp'), cs.get('maxhp'), cs.get('ac'), abil, wpn, ' · '.join(notes)))
    open(party_out, 'w', encoding='utf-8').write(
        '### 📊 파티 현황판 (%s · 게임에서 자동 추출)\n\n| 캐릭터 | 클래스 · 하위 | 역할 | 레벨 | HP | 방어도 | 능력치 (굵게 = 주 능력치) | 무기 | 상태 |\n|---|---|---|---|---|---|---|---|---|\n%s\n\n' % (date, '\n'.join(rowsP)))
parts.append('')
parts.insert(len(parts) - len(inv['chars']) - 1, '#### 👜 인벤토리별 전체 목록\n')
open(out, 'w', encoding='utf-8').write('\n'.join(parts))
print('sell', len(SELL_LIST), tot)
print('ok', sum(count(c.get('items')) for c in inv['chars']))
