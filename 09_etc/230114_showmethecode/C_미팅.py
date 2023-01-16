'''
< 미팅 >
문제)
- A대학 N명과 B대학 M명이 미팅을 하려고 한다.
- 길이가 긴 식탁 하나가 있다.
    - 한쪽에는 A, 다른쪽에는 B가 앉아있다.
- A : 1 ~ N
- B : 1 ~ M
- 의자에 않을때는 번호가 증가하는 순서대로 앉는다.
- 모든 일정이 끝나면 서로 악수를 한다.
- 한사람은 최대 한 사람과 악수 할 수 있다.
    - 팔이 교차하면 악수 X
    - 악수 하지 못하는 사람 있다
        - 즉 어떤 i( 1 <= i <= K)에 대해
        - i번째 쌍이 A대학의 Xi와 B대학의 Yi라고하면
        - Xi < Xj, Yi < Yj (1 <= j <= K)
- 학생의 성격을 1 ~ C까지의 정수로 나타낸다.
- 성격이 a인 사람은 성격이 b인 사람과 악수를 한다.
    - W[a][b] 만족도를 얻는다.
- 최대한 많은 만족도를 얻는 방법을 찾아라. 
입력)
- 1     : N, M, C
- 2[C]  : W[a][b] (1 <= a, b <= C)
- 3[N]  : A대학의 성격
- 4[M]  : B대학의 성격
'''
import sys
from itertools import combinations
input = sys.stdin.readline

N, M, C = map(int, input().split())
W = [list(map(int, input().split())) for _ in range(C)]
A = list(map(int, input().split())) # A대학의 성격 : 1 ~ N
B = list(map(int, input().split())) # B대학의 성격 : 1 ~ M



if N > M:
    for i in range(1, M + 1):
        a = combinations(A, i)
        b = combinations(B, i)
else:
    for i in range(1, N + 1):
        a = combinations(A, i)
        b = combinations(B, i)
