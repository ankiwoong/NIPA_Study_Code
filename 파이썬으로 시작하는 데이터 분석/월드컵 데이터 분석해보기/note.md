# 데이터 분석이란?

### 데이터 분석은 주어진 자료를 가공하여 원하는 정보와 결론을 얻어내는 일련의 처리 과정을 의미합니다.

### 데이터 분석은 보통 아래의 단계로 이루어집니다.

- 주제 선정
- 데이터 구조 파악
- 데이터 전처리
- 데이터 분석 구현

### 주제 선정

어떤 데이터를 선정할 지, 데이터에서 어떤 가설을 세우고 분석을 시작할 지, 어떤 결론을 원하는 지 등 데이터 분석의 목적을 세웁니다.

### 데이터 구조 파악

데이터를 분석하기 위해서, 데이터가 저장된 형태와 자료형, 변수 이름 등을 미리 파악해야 합니다.
또는 데이터 프레임에 통계량 함수를 적용하여, 데이터의 분포도나 성향 등을 파악할 수 있습니다.

### 데이터 전처리

데이터를 분석하기 전, 필요한 변수만을 추출하거나 기존의 변수로 새로운 변수를 계산하여 만들기도 합니다.
데이터의 결측값과 이상값이 있다면, 이 단계에서 올바르게 제거하여야 데이터 분석 결과를 올바르게 확인할 수 있습니다.

### 데이터 분석

주제 선정 단계에서 세운 가설을 numpy, pandas 등으로 데이터를 연산, 가공하여 가설을 입증하거나 원하는 정보를 얻어내는 것을 구현 하는 단계입니다.
얻어낸 정보를 효과적으로 보여주기 위해 시각화를 하기도 합니다.

---

실습에서 주어지는 월드컵 데이터 셋 WorldCups.csv의 칼럼은 다음과 같습니다.

출처 : https://www.kaggle.com/abecklas/fifa-world-cup

| 변수명         | 의미         | 예시       |
| -------------- | ------------ | ---------- |
| Year           | 개최 연도    | 1930       |
| Country        | 개최 국가    | Uruguay    |
| Winner         | 우승 국가    | Uruguay    |
| Runners-Up     | 준우승 국가  | Argentina  |
| Third          | 3위 국가     | USA        |
| Fourth         | 4위 국가     | Yugoslavia |
| GoalsScored    | 총 득점 수   | 70         |
| QualifiedTeams | 참가 국가 수 | 13         |
| MatchesPlayed  | 총 경기 수   | 18         |
| Attendance     | 총 관중      | 590549     |

---

실습에서 주어지는 월드컵 데이터 셋 WorldCupMatches.csv의 칼럼은 다음과 같습니다.

출처 : https://www.kaggle.com/abecklas/fifa-world-cup

| 변수명               | 의미                             | 예시                       |
| -------------------- | -------------------------------- | -------------------------- |
| Year                 | 경기가 진행된 연도               | 1930                       |
| Datetime             | 경기 시작 시간                   | 13 Jul 1930 - 15:00        |
| Stage                | 스테이지(조별리그, 16강, 8강 등) | Group 1                    |
| Stadium              | 경기장                           | Pocitos                    |
| City                 | 도시                             | Montevideo                 |
| Home Team Name       | 홈 팀 국가 이름                  | France                     |
| Home Team Goals      | 홈 팀 득점 수                    | 4                          |
| Away Team Goals      | 원정 팀 득점 수                  | 1                          |
| Away Team Name       | 원정 팀 국가 이름                | Mexico                     |
| Win conditions       | 승리 상황                        | Italy win after extra time |
| Attendance           | 관중 수                          | 4444                       |
| Half-time Home Goals | 홈 팀 전반전 득점 수             | 3                          |
| Half-time Away Goals | 원정 팀 전반전 득점 수           | 0                          |
| Referee              | 주심의 이름                      | LOMBARDI Domingo (URU)     |
| Assistant 1          | 제 1 부심(선심)의 이름           | CRISTOPHE Henry (BEL)      |
| Assistant 2          | 제 2 부심(선심)의 이름           | REGO Gilberto (BRA)        |
| RoundID              | 라운드의 고유 ID                 | 201                        |
| MatchID              | 경기의 고유 ID                   | 1096                       |
| Home Team Initials   | 홈 팀의 세 글자 이니셜           | FRA                        |
| Away Team Initials   | 원정 팀의 세 글자 이니셜         | MEX                        |
