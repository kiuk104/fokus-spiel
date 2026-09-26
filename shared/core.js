/* Fokus Spiel — 모든 페이지 공통: 테마·글자 크기 설정, 오프라인(서비스 워커), 새 버전 알림 */
(function(){
  var R=document.documentElement, ROOT=window.FS_ROOT||'';
  function get(k){try{return localStorage.getItem(k)}catch(e){return null}}
  function put(k,v){try{ v==null?localStorage.removeItem(k):localStorage.setItem(k,v) }catch(e){}}

  // settings: theme + font size (저장 키는 기존 붉은사막 노트와 같게 유지)
  var setBtn=document.getElementById('setBtn'), panel=document.getElementById('setPanel');
  function mark(seg,val){ [].forEach.call(document.querySelectorAll('#'+seg+' button'),function(b){b.setAttribute('aria-pressed',String(b.dataset.v===val))}); }
  function applyTheme(v){ if(v==='system'){R.removeAttribute('data-theme');put('cd-theme',null);} else {R.setAttribute('data-theme',v);put('cd-theme',v);} mark('segTheme',v); }
  function applyFs(v){ R.style.setProperty('--fs',v); put('cd-fs',v==='1'?null:v); mark('segFs',v); }
  if(setBtn&&panel){
    mark('segTheme', get('cd-theme')||'system'); mark('segFs', get('cd-fs')||'1');
    document.getElementById('segTheme').addEventListener('click',function(e){ var v=e.target.dataset&&e.target.dataset.v; if(v)applyTheme(v); });
    document.getElementById('segFs').addEventListener('click',function(e){ var v=e.target.dataset&&e.target.dataset.v; if(v)applyFs(v); });
    var togglePanel=function(open){ panel.hidden=!open; setBtn.setAttribute('aria-expanded',String(open)); };
    setBtn.addEventListener('click',function(e){ e.stopPropagation();
      if(panel.hidden){ var bp=document.getElementById('bmPanel'), bb=document.getElementById('bmBtn'); if(bp){bp.hidden=true;} if(bb){bb.setAttribute('aria-expanded','false');} }
      togglePanel(panel.hidden); });
    document.addEventListener('click',function(e){ if(!panel.hidden && !panel.contains(e.target) && !setBtn.contains(e.target)) togglePanel(false); });
    document.addEventListener('keydown',function(e){ if(e.key==='Escape' && !panel.hidden){ togglePanel(false); setBtn.focus(); } });
  }

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
