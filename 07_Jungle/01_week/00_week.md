# Jungle_01_week CheckPoint

### 4344
https://www.acmicpc.net/problem/4344
- 소수점 자릿수 출력
- round(x, 숫자)
    - 40.000 와같은 수는 출력안됨
- f'{숫자:.3f}'
- :.3f
    - 40.000 출력 OK!

### 2869
https://www.acmicpc.net/problem/2869
- 낮에 나무막대에 올라가는 감
- (도달 날짜 x일) : up:x번, down:x-1번
ax - b(x-1) >= v
ax - bx = v - b
- 5 4 7
5 - 4 + 5 - 4 + 5 >= 7
3
- 5 3 7
5 - 3 + 5 >= 7
- 5 2 7 
5 - 2 + 5 >= 6

### 9020 골드바흐의 추측
https://www.acmicpc.net/problem/9020
- 골드바흐의 추측(풀긴했지만 보자마자 못품)

### 1065 한수
https://www.acmicpc.net/problem/1065
- 문자열과 정수형 변환 주의

### 1914 하노이탑
https://www.acmicpc.net/problem/1914
- 마지막 조건(출력부분) 20보다 큰경우 과정 X 

### 9663 NQueen
https://www.acmicpc.net/problem/9663
- neg_diag, pos_diag, row_check : set() 이용

### 1074 Z
https://www.acmicpc.net/problem/1074
- 시간초과 발생 영역체크?
- **영역체크할때 return 빼먹어서 한시간동안 삽질함** 

### 10989 수정렬하기
https://www.acmicpc.net/problem/10989
- Count Array 이용 dict XXXX
- 숫자 범위 ~ [1 \ 10,000]
- Count Array : [0] * 10001

### 10819 차이를 최대로
https://www.acmicpc.net/problem/10819
- N범위 ~ [3 \ 8]
- 시간제한 1초
- 완탐일 확률 높음