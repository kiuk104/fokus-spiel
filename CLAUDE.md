# Fokus Spiel — 개인 게임 위키

GitHub Pages: https://kiuk104.github.io/fokus-spiel/ (main 브랜치 루트가 그대로 배포됨)
로컬 사본: `E:\Coding\fokus-spiel`

## 구조
- `games.json` — 게임 목록 (id, 이름, 허브 카드 문구, 상단 링크). 허브 카드 순서 = `playing: true` 먼저.
- `src/<id>/guide.md` — 게임별 원본 노트. **HTML을 직접 고치지 말고 md를 고친 뒤 빌드**한다.
- `src/<id>/status.html` — (선택) 가이드 맨 위 진행 현황 상자.
- `templates/` — guide.html · hub.html · sw.js 틀. `shared/` — 공통 CSS/JS (테마·검색·북마크·구글 로그인 동기화).
- 테마·폰트는 `bible_viewer` 와 같은 팔레트(라이트 #f2f3ef/청록 #255e66, 다크 #121514/금색 #d39c3c)와 Noto Serif KR + IBM Plex Sans KR 를 쓴다.
- `<id>/guide.html`, `index.html`, `sw.js`, `data/` — `build.py`가 만드는 결과물.
- `crimson-desert/checklist.html`, `infographic*.html` — 손으로 관리하는 붉은사막 전용 페이지.

## 노트 작성 규칙
- 문서는 `# 🖥️ PART 1 — 기술 세팅` 과 `# 🎮 PART 2 — 게임플레이 가이드` 로 나눈다.
- 퀘스트·질문 기록은 `## 진행 기록`(붉은사막은 `## 퀘스트 진행 기록`) 아래 `### Q번호. 제목 (날짜)` 로 이어 붙이고, 출처는 `## 참고 자료` 에 추가.
- md를 고치면 **항상 빌드 후 push** — md와 웹페이지는 늘 같은 내용이어야 한다.

## 붉은사막 원본 위치 (예외)
붉은사막 노트의 원본은 `E:\GameDev\Crimson-Desert\붉은사막살아남기\붉은사막_가이드.md` 이다.
빌드 전에 이 파일을 `src/crimson-desert/guide.md` 로 복사한다.

## 빌드 · 배포
```
pip install markdown
python build.py                # 전체
python build.py dark-souls     # 한 게임만
git add -A && git commit -m "..." && git push
```
Pages 반영은 약 1분. 페이지를 열어 둔 기기에는 "새 버전이 있어요" 알림이 뜬다.

## 새 게임 추가
1. `games.json` 에 항목 추가 (id는 영문 소문자-하이픈)
2. `src/<id>/guide.md` 작성 (위 규칙의 PART 1/2 뼈대)
3. `shared/fokus.css` 의 게임별 강조색 블록에 `[data-game="<id>"]` 라이트/다크 색 추가
4. (선택) `<id>/cover.jpg` — 허브 카드 썸네일용 대표 이미지(세로 2:3, 240×360 권장). 없으면 `mono` 글자 타일이 나온다.
5. `python build.py`

## 동기화 (Firebase `reddesert-checklist`)
문서 `checklists/{uid}` 하나에 필드로 나눠 저장: 붉은사막 북마크 `bookmarks`, 어비스 체크 `checked`, 다른 게임 북마크 `bm_<id(하이픈→_)>`.
