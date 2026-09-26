"""Fokus Spiel 빌드 — src/<게임>/guide.md 를 <게임>/guide.html 로 만들고, 허브·검색 색인·서비스 워커를 갱신한다.

사용:  python build.py            (전체)
       python build.py dark-souls (한 게임만 — 허브·색인·sw는 항상 다시 만든다)
필요:  pip install markdown
"""
import re, html, sys, json, os, hashlib, datetime, markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
NOW = datetime.datetime.now(datetime.timezone.utc)
BUILD = NOW.strftime('%Y%m%d%H%M%S')
TODAY = (NOW + datetime.timedelta(hours=2)).strftime('%Y-%m-%d')

games = json.load(open(P('games.json'), encoding='utf-8'))
meta_path = P('data', 'meta.json')
meta = json.load(open(meta_path, encoding='utf-8')) if os.path.exists(meta_path) else {}
only = sys.argv[1:]


def inline(t):
    return re.sub(r'^<p>|</p>$', '', markdown.markdown(t))


def render_body(body):
    text = '\n'.join(l for l in body if l.strip() != '---')
    text = re.sub(r'~~(.+?)~~', r'<del>\1</del>', text)
    h = markdown.markdown(text, extensions=['tables'])
    h = h.replace('<h4>', '<h5 class="ssub">').replace('</h4>', '</h5>')
    h = h.replace('<h5>', '<h6>')
    h = re.sub(r'<code>(.*?)</code>', r'<kbd>\1</kbd>', h, flags=re.S)
    h = h.replace('<table>', '<div class="tw"><table>').replace('</table>', '</table></div>')
    h = re.sub(r'<a href="(http[^"]+)">', r'<a href="\1" target="_blank" rel="noopener">', h)

    def bq(m):
        inner = m.group(1).strip()
        txt = re.sub('<[^>]+>', '', inner)
        cls = 'warn' if re.search('⚠️|주의|정정|❗', txt[:80]) else ('tip' if re.search('💡|⭐|🎁|꿀팁', txt[:40]) else 'note')
        return '<aside class="%s">%s</aside>' % (cls, inner)
    h = re.sub(r'<blockquote>(.*?)</blockquote>', bq, h, flags=re.S)
    return h.replace('\n', '')


def plain_text(s):
    t = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()


def live_links(g):
    """파일이 실제로 있는 링크만 (아직 안 올린 매뉴얼 등은 숨김)"""
    return [l for l in g.get('links', []) if os.path.exists(P(g['id'], l['href']))]


def build_game(g):
    md = open(P('src', g['id'], 'guide.md'), encoding='utf-8').read()
    lines = md.split('\n')
    assert lines[0].startswith('# '), 'md 첫 줄은 "# 제목" 이어야 해요'
    blocks, cur, in_code = [], [0, None, []], False
    for ln in lines[1:]:
        if ln.startswith('```'):
            in_code = not in_code
        m = None if in_code else re.match(r'^(#{1,3}) (.+)$', ln)
        if m:
            blocks.append(cur)
            cur = [len(m.group(1)), m.group(2).strip(), []]
        else:
            cur[2].append(ln)
    blocks.append(cur)

    nav, secs, index = [], [], []
    n = 0
    for lvl, title, body in blocks:
        bh = render_body(body)
        if lvl == 0:
            if not re.sub('<[^>]+>', '', bh).strip():
                continue
            bid, head, tplain = 'intro', '', '소개'
        else:
            n += 1
            pre, tag, cls, navc = {1: ('p', 'h2', 'part', 'nav0'), 2: ('s', 'h3', 'sec', 'nav1'), 3: ('q', 'h4', 'sub', 'nav2')}[lvl]
            bid = pre + str(n)
            th = inline(title)
            head = '<%s class="%s" id="%s">%s</%s>' % (tag, cls, bid, th, tag)
            tplain = plain_text(th)
            navtxt = html.escape(tplain.replace('🖥️ ', '').replace('🎮 ', ''))
            nav.append('<a class="%s" href="#%s">%s</a>' % (navc, bid, navtxt))
        ptxt = plain_text(head + bh)
        s_attr = html.escape(' ' + ptxt.lower() + ' ', quote=True)
        secs.append('<section class="blk" id="blk-%s" data-s="%s">%s%s</section>' % (bid, s_attr, head, bh))
        if lvl >= 2 or lvl == 0:
            index.append({'g': g['id'], 'h': bid, 't': tplain, 'x': plain_text(bh)[:1200]})

    qs = [int(x) for x in re.findall(r'^### Q(\d+)\.', md, flags=re.M)]
    qtxt = ('Q1–Q%d' % max(qs)) if qs else '기록 시작 전'
    src_note = g.get('source') or ('src/%s/guide.md' % g['id'])
    foot = '%s · %s<br>원본: %s — 문서가 갱신되면 이 페이지도 다시 발행됩니다.' % (html.escape(g['title']), qtxt, html.escape(src_note))

    status_p = P('src', g['id'], 'status.html')
    status = open(status_p, encoding='utf-8').read() if os.path.exists(status_p) else ''
    extra = ''
    for l in live_links(g):
        if l.get('label'):
            extra += '    <a class="btn xlink" href="%s">%s</a>\n' % (l['href'], html.escape(l['label']))

    fsg = {'id': g['id']}
    if g.get('keys'):
        fsg['keys'] = g['keys']
    if g.get('cloudField'):
        fsg['cloudField'] = g['cloudField']

    tpl = open(P('templates', 'guide.html'), encoding='utf-8').read()
    rep = {
        'GAME_ID': g['id'], 'TITLE': html.escape(g['title']), 'GAME_EN': html.escape(g['en']),
        'BRAND_SUB': html.escape(g.get('brand_sub', '')), 'DESC': html.escape(g.get('desc', ''), quote=True),
        'BUILD': BUILD, 'V': BUILD, 'NAV': '\n'.join(nav), 'STATUS': status, 'CONTENT': '\n'.join(secs),
        'FOOT': foot, 'EXTRA_LINKS': extra, 'SEARCH_HINT': html.escape(g.get('search_hint', '검색'), quote=True),
        'FSG_JSON': json.dumps(fsg, ensure_ascii=False),
    }
    out = re.sub(r'\{\{([A-Z_]+)\}\}', lambda m: rep[m.group(1)], tpl)
    os.makedirs(P(g['id']), exist_ok=True)
    open(P(g['id'], 'guide.html'), 'w', encoding='utf-8').write(out)

    h = hashlib.sha1(md.encode('utf-8')).hexdigest()
    m = meta.get(g['id'], {})
    if m.get('hash') != h:
        m = {'hash': h, 'updated': TODAY}
    m.update({'q': len(qs), 'sections': sum(1 for b in blocks if b[0] in (2, 3)), 'qmax': max(qs) if qs else 0})
    meta[g['id']] = m
    print('%-26s blocks %3d  Q %3d' % (g['id'], len(secs), len(qs)))
    return index


def build_hub():
    order = [g for g in games if g.get('playing')] + [g for g in games if not g.get('playing')]
    cards = []
    for g in order:
        m = meta.get(g['id'], {})
        stat = ('기록 Q%d까지' % m['qmax']) if m.get('qmax') else '기록 시작 전'
        links = ''.join('<a href="%s/%s">%s</a>' % (g['id'], l['href'], html.escape(l['hub'])) for l in live_links(g))
        badge = '<span class="badge">플레이 중</span>' if g.get('playing') else ''
        cards.append(
            '<article class="card" data-game="%(id)s">'
            '<a class="card-main" href="%(id)s/guide.html">'
            '<span class="mono" aria-hidden="true">%(mono)s</span>'
            '<span class="card-tx"><span class="card-en">%(en)s</span><span class="card-name">%(name)s</span>'
            '<span class="card-title">%(title)s</span></span></a>'
            '<div class="card-ft"><span class="card-stat">%(badge)s%(stat)s · %(upd)s 갱신</span>%(links)s</div>'
            '</article>' % {'id': g['id'], 'mono': html.escape(g['mono']), 'en': html.escape(g['en']),
                            'name': html.escape(g['name']), 'title': html.escape(g['title']), 'badge': badge,
                            'stat': stat, 'upd': (m.get('updated', TODAY)[5:].replace('-', '.')),
                            'links': ('<span class="card-links">%s</span>' % links) if links else ''})
    names = {g['id']: g['name'] for g in games}
    tpl = open(P('templates', 'hub.html'), encoding='utf-8').read()
    rep = {'BUILD': BUILD, 'V': BUILD, 'CARDS': '\n'.join(cards), 'COUNT': str(len(games)),
           'NAMES': json.dumps(names, ensure_ascii=False)}
    open(P('index.html'), 'w', encoding='utf-8').write(re.sub(r'\{\{([A-Z_]+)\}\}', lambda m: rep[m.group(1)], tpl))


def build_sw():
    core = ['./', './index.html', './manifest.webmanifest', './shared/fokus.css', './shared/core.js',
            './shared/guide.js', './shared/sync.js', './icons/icon-192.png', './icons/favicon.svg']
    core += ['./%s/guide.html' % g['id'] for g in games]
    tpl = open(P('templates', 'sw.js'), encoding='utf-8').read()
    open(P('sw.js'), 'w', encoding='utf-8').write(tpl.replace('{{BUILD}}', BUILD).replace('{{CORE}}', json.dumps(core)))


if __name__ == '__main__':
    search = json.load(open(P('data', 'search.json'), encoding='utf-8')) if os.path.exists(P('data', 'search.json')) else []
    for g in games:
        if only and g['id'] not in only:
            continue
        idx = build_game(g)
        search = [s for s in search if s['g'] != g['id']] + idx
    known = {g['id'] for g in games}
    search = [s for s in search if s['g'] in known]
    os.makedirs(P('data'), exist_ok=True)
    json.dump(search, open(P('data', 'search.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    json.dump(meta, open(meta_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    build_hub()
    build_sw()
    print('build', BUILD)
