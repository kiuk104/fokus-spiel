"""생성한 표를 모바일에서 카드 형태로 보이게: <table class="cards"> + 각 td 에 data-label"""
import re, sys
STYLE = '''<style>
@media (max-width:760px){
 table.cards{width:100%!important;min-width:0!important;font-size:13px!important}
 table.cards thead{display:none}
 table.cards tr{display:block;padding:7px 10px;border-bottom:1px solid var(--line);line-height:1.4}
 table.cards tr:last-child{border-bottom:0}
 table.cards td{display:inline-block;max-width:none!important;padding:0!important;border:0!important;white-space:normal!important;text-align:left!important;margin:0 10px 0 0;vertical-align:baseline}
 table.cards td[data-label]:not([data-label=""])::before{content:attr(data-label);margin-right:4px;opacity:.5;font-size:11px}
 table.cards td.ic{float:left;margin:1px 9px 0 0}
 table.cards td.ic img{width:30px!important;height:30px!important}
 table.cards td.ic:empty{display:none}
 table.cards td.nm{display:block;font-weight:600;font-size:14px}
 table.cards td.en{display:block;opacity:.7;font-size:12px}
 table.cards td.nm::before,table.cards td.en::before{display:none!important}
 table.cards td:empty{display:none}
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
                elif lab == '영문 이름': cls = ' class="en"'
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
