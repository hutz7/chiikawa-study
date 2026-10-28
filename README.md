# 정보처리기사 실기 개념 퀴즈

2020~2025년 실기 복원 자료의 주제를 바탕으로 만든 짧은 문답 289개입니다.
기출 원문·전 문항이 아닌 기출 단서 변형과 관련 보강 문제를 포함합니다.

- 전체 랜덤 / 2020~2025년 연도별 묶음
- 20·50·100문제 선택 (묶음 수보다 많으면 묶음 전체)
- 단답 입력·자동 채점·해설·오답 복습·이어풀기
- 브라우저에 저장되는 개인별 진도

## 바로 열기
index.html을 브라우저로 열어 학습 모드를 고릅니다. 코드 학습의 CSS/JS 파일도 함께 있어야 합니다.
기존 개념 문답만 단일 파일로 이용하려면 concepts.html을 열면 됩니다.
파일로 열 때의 기록 저장은 브라우저 지원에 따라 달라질 수 있습니다.

## GitHub Pages 배포
1. GitHub에서 공개 저장소를 만듭니다. 예: chiikawa-study
2. HTML·CSS·JS 등 제공된 사이트 파일을 저장소 최상위에 업로드하고 커밋합니다.
3. 저장소 Settings → Pages로 이동합니다.
4. Build and deployment → Source: Deploy from a branch를 선택합니다.
5. Branch: main, Folder: /(root)를 선택하고 Save를 누릅니다.
6. Pages에 표시되는 주소로 접속합니다.

공식 안내: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## 학습 기록과 연도
진도는 현재 기기·브라우저·주소에 저장됩니다. 다른 주소로 옮길 때 자동 동기화되지 않습니다.
연도는 각 문항의 참고 복원 회차 기준이며, 연도별 문항 수는 실제 시험 문항 수가 아닙니다.
캐릭터 일러스트는 비공식 팬 테마이며 공식 서비스가 아닙니다.

## 코드 이해 학습
첫 화면에서 개념 문답과 코드 이해 학습을 선택할 수 있습니다.
기존 단일 파일 개념 문답은 `concepts.html`에 그대로 보존했습니다.
`code-study.html`에서 C 7개, Java 6개, Python 5개 문법 주제를 학습합니다.

- 출력 예측 → 중간 값 → 이유 선택 → 문법 해설·단계별 실행 추적
- 값·분기·참조 관계·호출 타입 등을 바꾸는 학습용 변형 (기출 원문 아님)
- 다른 구조 두 종류를 도움 없이 통과하면 이해 확인으로 기록
- 오답 주제 복습, 언어·진도 필터, 답안 자동 저장·이어풀기
- 기존 개념 문답의 `info-pocket-v1`과 분리된 `info-code-understanding-v1` 저장 키
- 두 학습 모드 모두 같은 기기·브라우저의 localStorage 사용, 계정 동기화 없음

문항 검증: `python tests/verify-generated.py` (Node, Python, gcc, Java 17 필요).
18개 주제 × 8개 변형 = 144개 코드의 실제 출력과 등록 정답을 대조합니다.

GitHub Pages에는 저장소 루트의 파일을 그대로 배포합니다.
첫 화면 및 코드 학습에는 함께 제공하는 CSS/JS 파일이 필요합니다.
개념 문답 단일 파일만 이용하려면 `concepts.html`을 열면 됩니다.
