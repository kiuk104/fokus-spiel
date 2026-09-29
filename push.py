"""Fokus Spiel push — 원격에 다른 세션 커밋이 있으면 먼저 rebase 하고 push 한다.
사용:  python push.py            (커밋은 미리 해 둔다)
       python push.py -m "메시지"  (미커밋 변경을 이 메시지로 커밋한 뒤 push)
빌드 결과물은 git 에 없으므로(.gitignore) 충돌은 원본 파일이 정말 겹칠 때만 난다. 그때는 멈추고 알려준다.
"""
import subprocess, sys, os
ROOT = os.path.dirname(os.path.abspath(__file__))
def git(*a, check=True):
    r = subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
    if check and r.returncode:
        print(r.stdout + r.stderr); sys.exit('git %s 실패' % a[0])
    return r
args = sys.argv[1:]
if args[:1] == ['-m']:
    if git('status', '--porcelain').stdout.strip():
        git('add', '-A'); git('commit', '-q', '-m', args[1]); print('커밋:', args[1])
elif git('status', '--porcelain').stdout.strip():
    sys.exit('미커밋 변경이 있어요. 먼저 커밋하거나  python push.py -m "메시지"  로 실행하세요.\n' + git('status', '--short').stdout)
git('fetch', 'origin')
behind = git('rev-list', '--count', 'HEAD..origin/main').stdout.strip()
if behind != '0':
    print('원격에 새 커밋 %s개 — rebase 합니다.' % behind)
    r = git('rebase', 'origin/main', check=False)
    if r.returncode:
        conflicted = git('diff', '--name-only', '--diff-filter=U').stdout.split()
        git('rebase', '--abort', check=False)
        sys.exit('원본 파일이 다른 세션과 겹쳤어요 — 손으로 합쳐야 합니다:\n  ' + '\n  '.join(conflicted)
                 + '\n(git pull --rebase 후 충돌을 정리하고 다시 push 하세요)')
ahead = git('rev-list', '--count', 'origin/main..HEAD').stdout.strip()
if ahead == '0':
    print('올릴 커밋이 없어요. (원격과 같음)'); sys.exit()
git('push', 'origin', 'main')
print('push 완료 — 커밋 %s개. 1~3분 뒤 Actions 가 빌드해서 Pages 에 올립니다: https://github.com/kiuk104/fokus-spiel/actions' % ahead)
