"""생성한 표를 모바일에서 카드 형태로 보이게: <table class="cards"> + 각 td 에 data-label"""
import re, sys
STYLE = '''<style>
@media (max-width:760px){
 table.cards{width:100%!important;min-width:0!important}
 table.cards thead{display:none}
 table.cards tr{display:block;padding:10px 12px;border-bottom:1px solid var(--line)}
 table.cards tr:last-child{border-bottom:0}
 table.cards td{display:block;max-width:none!important;padding:1px 0!important;border:0!important;white-space:normal!important;text-align:left!important}
 table.cards td[data-label]:not([data-label=""])::before{content:attr(data-label);display:inline-block;min-width:5.5em;margin-right:8px;opacity:.55;font-size:11.5px}
 table.cards td.ic{float:left;margin:2px 10px 4px 0}
 table.cards td.ic:empty{display:none}
 table.cards td.nm{font-weight:600}
 table.cards td.nm::before{display:none!important}
 table.cards tr::after{content:"";display:block;clear:both}
}
</style>
<script>
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('table:not(.cards)').forEach(function (t) {
    var h = Array.prototype.map.call(t.querySelectorAll('thead th'), function (x) { return x.textContent.trim(); });
    if (!h.length) return;
    t.classList.add('cards');
    t.querySelectorAll('tbody tr').forEach(function (r) {
      Array.prototype.forEach.call(r.children, function (c, i) {
        if (c.tagName !== 'TD') return;
        c.setAttribute('data-label', h[i] || '');
        if (i === 0) c.classList.add('nm');
      });
    });
  });
});
</script>
'''
def cardify(html):
    def fix(m):
        t = m.group(0)
        heads = [re.sub('<[^>]+>', '', h).strip() for h in re.findall(r'<th[^>]*>(.*?)</th>', t, re.S)]
        t = t.replace('<table>', '<table class="cards">', 1)
        def row(rm):
            r = rm.group(0)
            if 'colspan' in r: return r
            i = [0]
            def cell(cm):
                idx = i[0]; i[0] += 1
                lab = heads[idx] if idx < len(heads) else ''
                attrs = cm.group(1) or ''
                cls = ''
                if lab == '' : cls = ' class="ic"'
                elif lab == '한글 이름' or (lab == '종류' and idx == 0): cls = ' class="nm"'
                return '<td%s data-label="%s"%s>' % (attrs, lab, cls)
            return re.sub(r'<td((?:\s+style="[^"]*")?)>', cell, r)
        return re.sub(r'<tr>(?:(?!</tr>).)*</tr>', row, t, flags=re.S)
    return re.sub(r'<table>(?:(?!</table>).)*</table>', fix, html, flags=re.S)
if __name__ == '__main__':
    for p in sys.argv[1:]:
        s = open(p, encoding='utf-8').read()
        s = cardify(s)
        if p.endswith('inv_section.md'): s = STYLE + s
        open(p, 'w', encoding='utf-8').write(s)
