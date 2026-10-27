"""fokus_inventory.json (Script Extender 내보내기) → 위키용 인벤토리 목록 HTML 조각"""
import json, pickle, sys, html, collections, os
S = os.path.dirname(os.path.abspath(__file__))
inv = json.load(open(sys.argv[1], encoding='utf-8'))
date = sys.argv[2]; icon_dir = sys.argv[3]; out = sys.argv[4]
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
ORDER = {c: i for i, (c, _) in enumerate(CATS)}; ORDER['기타'] = 99
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
def rows(items):
    g = collections.OrderedDict()
    for x in items or []:
        if 'err' in x: continue
        if x.get('items'): continue   # 가방은 따로 섹션으로
        key = (x.get('h'), x.get('stats'), x.get('name'))
        if key not in g: g[key] = [x, 0]
        g[key][1] += x.get('amount') or 1
    lst = sorted(g.values(), key=lambda v: (ORDER[cat(v[0].get('stats'))], names(v[0])[0] or names(v[0])[1]))
    out = []
    for x, n in lst:
        k, e = names(x)
        badge = ' <span title="이야기 아이템" style="color:#c96a12">◆</span>' if x.get('story') else ''
        out.append('<tr><td>%s</td><td>%s%s</td><td>%s</td><td style="text-align:right">%s</td><td>%s</td></tr>' % (
            img(x), html.escape(k) if k else '<span style="opacity:.6">(한글 없음)</span>', badge, html.escape(e or ''), n, cat(x.get('stats'))))
    return out
def table(r):
    return ('<table><thead><tr><th></th><th>한글 이름</th><th>영문 이름</th><th>개수</th><th>종류</th></tr></thead><tbody>%s</tbody></table>' % ''.join(r))
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
    top = rows(c.get('items'))
    if top: body.append('<p><b>가방 밖</b></p>' + table(top))
    for x in sorted([x for x in c.get('items') or [] if x.get('items')], key=lambda x: names(x)[0] or names(x)[1]):
        k, e = names(x)
        label = (k + ' · ' + e) if k else e
        sub = rows(x.get('items'))
        nested = [y for y in x.get('items') if y.get('items')]
        for y in nested:
            sub += ['<tr><td colspan="5"><i>└ %s 안</i></td></tr>' % html.escape(names(y)[0] or names(y)[1])] + rows(y.get('items'))
        body.append('<p>%s <b>%s</b> <span style="opacity:.6">(%d)</span></p>' % (img(x), html.escape(label), count(x.get('items'))) + table(sub))
    gold = sum((x.get('amount') or 0) for x in walk(c.get('items')) if x.get('stats') == 'OBJ_GoldPile')
    parts.append('<details><summary><b>%s</b> — 아이템 %d개%s</summary>\n\n%s\n\n</details>\n' % (html.escape(who), total, (' · 금화 %d' % gold) if gold else '', '\n'.join(body)))
open(out, 'w', encoding='utf-8').write('\n'.join(parts))
print('ok', sum(count(c.get('items')) for c in inv['chars']))
