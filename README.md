git commit 관련 내용 정리
-> https://wikidocs.net/75555 참고

*작업한 내용을 원격 저장소에 저장하는 순서 간단 정리
1. 프로그램 변경 작업하기
2. git add <파일명> 또는 git add * 명령 수행하기
3. git commit -m "변경사항 요약" 명령 수행하기
4. git push 명령 수행하기

4번 수행할 때 fatal: couldn't find remote ref main 오류 지속 발생
- git show-ref 로 master인지 main인지 맨 마지막 단어 확인
- 나는 master를 main으로 변경 위해: git branch -m master main
- 그 후, git push origin main 실행!

git init - git status - .gitignore 파일 생성 - git add * - git status - git commit -m "메시지" - 파일 변경 후 git diff - 한글 깨지면 set LC_ALL=C.UTF-8 - git restore templates/base.html - git log
-> git remote add origin https://github.com/pahkey/pybo.git - git push -u origin main
