/* Fokus Spiel — 모든 페이지 공통: 테마·글자 크기 설정, 오프라인(서비스 워커), 새 버전 알림 */
(function(){
  var R=document.documentElement, ROOT=window.FS_ROOT||'';
  function get(k){try{return localStorage.getItem(k)}catch(e){return null}}
  function put(k,v){try{ v==null?localStorage.removeItem(k):localStorage.setItem(k,v) }catch(e){}}

  // settings: theme + font size (저장 키는 기존 붉은사막 노트와 같게 유지)
  var setBtn=document.getElementById('setBtn'), panel=document.getElementById('setPanel');
  function mark(seg,val){ [].forEach.call(document.querySelectorAll('#'+seg+' button'),function(b){b.setAttribute('aria-pressed',String(b.dataset.v===val))}); }
  var THEMES=[['system','시스템','',''],['light','밝게','#f2f3ef','#1b211f'],['paper','종이','#ece4d4','#2a2219'],['sepia','세피아','#cfc9bb','#3a3733'],['dim','진회색','#2b2d31','#e6e6e8'],['dark','검정','#121514','#e1e5df']];
  function syncMeta(){ var bg=getComputedStyle(document.body).backgroundColor; [].forEach.call(document.querySelectorAll('meta[name="theme-color"]'),function(m){m.content=bg;}); }
  function applyTheme(v){ if(v==='system'){R.removeAttribute('data-theme');put('cd-theme',null);} else {R.setAttribute('data-theme',v);put('cd-theme',v);} mark('segTheme',v); syncMeta(); }
  function themeGrid(){ var seg=document.getElementById('segTheme'); if(!seg) return; seg.className='thg';
    seg.innerHTML=THEMES.map(function(t){ return '<button type="button" data-v="'+t[0]+'"'+(t[0]==='system'?' class="sys"':' style="--tb:'+t[2]+';--ti:'+t[3]+'"')+'><b>가 Aa</b><small>'+t[1]+'</small></button>'; }).join(''); }
  function fontRows(){ var F=window.FS_FONTS, fsRow=document.getElementById('segFs'); if(!F||!fsRow) return; fsRow=fsRow.parentNode;
    [['cd-fbody','본문 글꼴',F.BODY,'plex'],['cd-fdisp','제목 글꼴',F.DISP,'noto']].forEach(/* 뒤에서부터 끼워 넣으므로 역순 */function(c){
      var row=document.createElement('div'); row.className='sp-row'; var lab=document.createElement('span'); lab.className='sp-lab'; lab.textContent=c[1]; row.appendChild(lab);
      var pk=document.createElement('div'); pk.className='fpk'; pk.setAttribute('role','group'); pk.setAttribute('aria-label',c[1]);
      function paint(){ var cur=get(c[0])||c[3]; [].forEach.call(pk.children,function(b){ b.setAttribute('aria-pressed',String(b.dataset.k===cur)); }); }
      Object.keys(c[2]).forEach(function(k){ var f=c[2][k], b=document.createElement('button'); b.type='button'; b.dataset.k=k;
        b.innerHTML='<b style="font-family:'+f[2].replace(/"/g,'&quot;')+'">'+f[0]+'</b>'+(f[1]?'<small>'+f[1]+'</small>':''); pk.appendChild(b); });
      pk.addEventListener('click',function(e){ var b=e.target.closest('button'); if(!b) return; put(c[0],b.dataset.k===c[3]?null:b.dataset.k); F.apply(); paint(); });
      // 고르기 전에도 미리보기가 그 글꼴로 보이게, 패널을 처음 열 때 전부 불러온다 (한 번 받으면 캐시)
      row.addEventListener('fs-open',function(){ Object.keys(c[2]).forEach(function(k){ F.load(c[2][k]); }); },{once:true});
      paint(); row.appendChild(pk); fsRow.parentNode.insertBefore(row,fsRow.nextSibling);
    }); }
  function applyFs(v){ R.style.setProperty('--fs',v); put('cd-fs',v==='1'?null:v); mark('segFs',v); }
  if(setBtn&&panel){
    themeGrid(); fontRows(); mark('segTheme', get('cd-theme')||'system'); mark('segFs', get('cd-fs')||'1'); syncMeta();
    document.getElementById('segTheme').addEventListener('click',function(e){ var b=e.target.closest('button'); if(b&&b.dataset.v)applyTheme(b.dataset.v); });
    document.getElementById('segFs').addEventListener('click',function(e){ var v=e.target.dataset&&e.target.dataset.v; if(v)applyFs(v); });
    var togglePanel=function(open){ panel.hidden=!open; setBtn.setAttribute('aria-expanded',String(open)); if(open) [].forEach.call(panel.querySelectorAll('.sp-row'),function(r){ r.dispatchEvent(new Event('fs-open')); }); };
    setBtn.addEventListener('click',function(e){ e.stopPropagation();
      if(panel.hidden){ var bp=document.getElementById('bmPanel'), bb=document.getElementById('bmBtn'); if(bp){bp.hidden=true;} if(bb){bb.setAttribute('aria-expanded','false');} }
      togglePanel(panel.hidden); });
    document.addEventListener('click',function(e){ if(!panel.hidden && !panel.contains(e.target) && !setBtn.contains(e.target)) togglePanel(false); });
    document.addEventListener('keydown',function(e){ if(e.key==='Escape' && !panel.hidden){ togglePanel(false); setBtn.focus(); } });
  }

  // install as app — 허브 상단 버튼 + 설정 창 "앱" 줄. 이미 앱으로 열려 있으면 숨김
  (function(){
    var standalone=(window.matchMedia&&matchMedia('(display-mode: standalone)').matches)||navigator.standalone===true;
    if(standalone) return;
    var ua=navigator.userAgent, ios=/iPhone|iPad|iPod/.test(ua)||(/Macintosh/.test(ua)&&navigator.maxTouchPoints>1);
    var deferred=null, btns=[], help=null;
    function mk(cls,label){ var b=document.createElement('button'); b.type='button'; b.className=cls; b.innerHTML=label; b.hidden=true; b.addEventListener('click',install); btns.push(b); return b; }
    function show(on){ btns.forEach(function(b){ b.hidden=!on; }); }
    function say(t){ if(!help) return; help.textContent=t; help.hidden=false; }
    function install(e){ if(e) e.stopPropagation();
      if(deferred){ deferred.prompt(); deferred.userChoice.then(function(r){ if(r&&r.outcome==='accepted') show(false); deferred=null; }); return; }
      if(ios) say('Safari 아래쪽 공유 버튼(□↑) → "홈 화면에 추가"를 누르세요.');
      else say('브라우저 메뉴(⋮)에서 "앱 설치" 또는 "홈 화면에 추가"를 누르세요. 주소창 오른쪽의 설치 아이콘(⊕)으로도 할 수 있어요.');
      if(setBtn&&panel&&panel.hidden) setBtn.click();
    }
    var dl='<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-2px;margin-right:5px"><path d="M12 4v11"/><path d="M7 10l5 5 5-5"/><path d="M5 20h14"/></svg>';
    // 설정 창 "앱" 줄 (모든 페이지)
    var app=document.querySelector('#setPanel .sp-app');
    if(app){ var row=app.parentNode, b=mk('',dl+'앱으로 설치'); b.id='installBtn2'; app.insertBefore(b,app.firstChild);
      help=document.createElement('p'); help.className='sp-note'; help.hidden=true; row.appendChild(help); }
    // 허브 상단 바
    var top=document.querySelector('.hub-top .in');
    if(top&&setBtn){ var t=mk('btn',dl+'앱 설치'); t.id='installBtn'; t.style.cssText='height:34px;display:inline-flex;align-items:center;white-space:nowrap'; top.insertBefore(t,setBtn); }
    addEventListener('beforeinstallprompt',function(e){ e.preventDefault(); deferred=e; show(true); });
    addEventListener('appinstalled',function(){ deferred=null; show(false); if(help) help.hidden=true; });
    // 설치 이벤트가 없는 브라우저(iOS Safari 등)는 설정 창에만 안내 버튼을 둔다
    if(ios){ show(true); }
    else setTimeout(function(){ if(!deferred){ btns.forEach(function(b){ if(b.id==='installBtn2') b.hidden=false; }); } },3000);
  })();

  // offline
  if('serviceWorker' in navigator){ addEventListener('load',function(){ navigator.serviceWorker.register(ROOT+'sw.js',{scope:ROOT||'./'}).catch(function(){}); }); }

  // new version check — 설치한 앱에서도 새로고침 없이 업데이트
  var me=(document.querySelector('meta[name="cd-build"]')||{}).content||'';
  var page=location.pathname.split('/').pop()||'index.html';
  var info=document.getElementById('buildInfo');
  if(info&&me){ var d=new Date(Date.UTC(+me.slice(0,4),+me.slice(4,6)-1,+me.slice(6,8),+me.slice(8,10),+me.slice(10,12))); var z=function(n){return (n<10?'0':'')+n}; info.textContent='버전 '+z(d.getMonth()+1)+'/'+z(d.getDate())+' '+z(d.getHours())+':'+z(d.getMinutes()); }
  function go(){ try{ if(navigator.serviceWorker&&navigator.serviceWorker.controller){ caches.keys().then(function(ks){ return Promise.all(ks.map(function(k){return caches.delete(k)})); }).finally(function(){ location.reload(); }); return; } }catch(e){} location.reload(); }
  var rb=document.getElementById('reloadBtn'); if(rb) rb.addEventListener('click',go);
  var toast=document.createElement('div'); toast.className='upd-toast'; toast.setAttribute('role','status'); toast.hidden=true;
  toast.innerHTML='<span>새 버전이 있어요</span><button type="button">업데이트</button><button type="button" class="x" aria-label="닫기">✕</button>';
  document.body.appendChild(toast);
  var dismissed=false, busy=false;
  toast.children[1].addEventListener('click',go);
  toast.children[2].addEventListener('click',function(){ toast.hidden=true; dismissed=true; });
  function check(){
    if(busy||dismissed||!me||!navigator.onLine) return; busy=true;
    fetch(page+'?v='+Date.now(),{cache:'no-store'}).then(function(r){return r.ok?r.text():''}).then(function(t){
      var m=t.match(/<meta name="cd-build" content="(\d+)"/); if(m&&m[1]>me) toast.hidden=false;
    }).catch(function(){}).finally(function(){ busy=false; });
  }
  setTimeout(check,2500);
  document.addEventListener('visibilitychange',function(){ if(document.visibilityState==='visible') check(); });
  window.addEventListener('online',check);
})();
