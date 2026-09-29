# Fokus Spiel — 개인 게임 위키

GitHub Pages: https://kiuk104.github.io/fokus-spiel/ (main 브랜치 루트가 그대로 배포됨)
로컬 사본: `E:\Coding\fokus-spiel`

## 구조
- `games.json` — 게임 목록 (id, 이름, 허브 카드 문구, 상단 링크). 허브 카드 순서 = `playing: true` 먼저.
- `src/<id>/guide.md` — 게임별 원본 노트. **HTML을 직접 고치지 말고 md를 고친 뒤 빌드**한다.
- `src/<id>/status.json` — (선택) 진행 현황. 빌드가 가이드 맨 위 상자 + 허브 카드 한 줄 + 사이드바 부제(`sub`)로 만든다. 게임별 Claude 프로젝트가 이 파일을 갱신한다.
  ```json
  {"sub": "Chapter 6 · Day 39", "where": "에르난드 공국 · 유니콘 절벽", "updated": "2026-09-26",
   "stats": [{"k": "메인", "v": 1, "max": 6}, {"k": "어비스 흔적", "v": 3, "max": 40, "hot": true},
             {"k": "숙련", "v": 0, "unit": "%"}, {"k": "현재 보스", "v": "오른스타인"}]}
  ```
  `v`가 숫자+`max`면 막대, `unit:"%"`면 퍼센트 막대, 문자열이면 글자만. `hot:true`는 강조색. 허브 카드 막대는 첫 번째 막대 항목.
  (예전 `status.html`은 json이 없을 때만 쓰임)
- `templates/` — guide.html · hub.html · sw.js 틀. `shared/` — 공통 CSS/JS (테마·검색·북마크·구글 로그인 동기화).
- 테마·폰트는 `bible_viewer` 와 같은 팔레트(라이트 #f2f3ef/청록 #255e66, 다크 #121514/금색 #d39c3c)와 Noto Serif KR + IBM Plex Sans KR 를 쓴다.
  설정 패널에서 테마 6종(시스템/밝게/종이/세피아/진회색/검정 — `data-theme`)과 제목·본문 글꼴을 고를 수 있다. 글꼴 목록은 `shared/fonts.js`(bible_viewer 와 같은 출처), 저장 키 `cd-theme` `cd-fdisp` `cd-fbody`. 새 테마를 추가하면 fokus.css 의 `:root:not([data-theme=…])` 목록과 checklist.html 에도 같이 넣는다.
- `<id>/guide.html`, `index.html`, `sw.js`, `data/` — `build.py`가 만드는 결과물. **git 에 없음**(Actions 가 만든다). 갱신일은 md 의 마지막 커밋 날짜.
- `crimson-desert/checklist.html`, `infographic*.html` — 손으로 관리하는 붉은사막 전용 페이지.

## 노트 작성 규칙
- 문서는 `# 🖥️ PART 1 — 기술 세팅` 과 `# 🎮 PART 2 — 게임플레이 가이드` 로 나눈다.
- 퀘스트·질문 기록은 `## 진행 기록`(붉은사막은 `## 퀘스트 진행 기록`) 아래 `### Q번호. 제목 (날짜)` 로 이어 붙이고, 출처는 `## 참고 자료` 에 추가.
- md를 고치면 **항상 빌드 후 push** — md와 웹페이지는 늘 같은 내용이어야 한다.

## 외부 원본 (games.json `source`)
`games.json`에 `source` 경로가 있으면 `build.py`가 빌드 전에 그 파일을 `src/<id>/guide.md`로 **자동 복사**한다(내용이 다를 때만).
현재 붉은사막만 해당: `E:\GameDev\Crimson-Desert\붉은사막살아남기\붉은사막_가이드.md`. 손으로 복사할 필요 없음.
`push.py` 도 push 전에 같은 복사를 하므로, 빌드 없이 push 해도 사본은 항상 최신이다. 원본은 옮기지 않아도 된다(Actions 는 커밋된 사본으로 빌드).

## 게임별 Claude 프로젝트와의 역할 분담
- 게임 프로젝트(다크소울, 굶지마 등)는 자기 게임의 `src/<id>/guide.md`(진행 기록)와 `src/<id>/status.json`만 고치고 `python build.py <id>` → push 한다.
- 이 프로젝트(fokus-spiel)는 템플릿·build.py·CSS·games.json 등 공통 구조와 세션 충돌 정리를 맡는다.
- 두 세션이 같은 시각에 push 할 수 있으니, 커밋 전 `git status`로 남의 미커밋 변경이 섞였는지 확인.

## 빌드 · 배포
빌드 결과물(`<id>/guide.html`, `index.html`, `sw.js`, `data/`)은 **git 에 넣지 않는다**(.gitignore). push 하면 GitHub Actions(`.github/workflows/pages.yml`)가 `build.py` 를 돌려 Pages 에 올린다(2~3분). 그래서 세션들이 원본 파일만 커밋하면 서로 충돌할 일이 없다.
```
pip install markdown
python build.py                # 로컬 미리보기용 (선택) — 전체
python build.py dark-souls     # 한 게임만
git add -A && git commit -m "..."
python push.py                 # fetch → 필요하면 rebase → push  (push_github.bat 과 같음)
python push.py -m "메시지"      # 커밋까지 한 번에
```
`push.py` 는 원격에 다른 세션 커밋이 있으면 알아서 rebase 한다. 원본 파일이 정말 겹치면 멈추고 파일 목록을 알려준다.
페이지를 열어 둔 기기에는 배포 뒤 "새 버전이 있어요" 알림이 뜬다.

## 새 게임 추가
1. `games.json` 에 항목 추가 (id는 영문 소문자-하이픈)
2. `src/<id>/guide.md` 작성 (위 규칙의 PART 1/2 뼈대)
3. `shared/fokus.css` 의 게임별 강조색 블록에 `[data-game="<id>"]` 라이트/다크 색 추가
4. (선택) `<id>/cover.jpg` — 허브 카드 썸네일용 대표 이미지(세로 2:3, 240×360 권장). 없으면 `mono` 글자 타일이 나온다.
5. `python build.py`

## 동기화 (Firebase `reddesert-checklist`)
문서 `checklists/{uid}` 하나에 필드로 나눠 저장: 붉은사막 북마크 `bookmarks`, 어비스 체크 `checked`, 다른 게임 북마크 `bm_<id(하이픈→_)>`.
