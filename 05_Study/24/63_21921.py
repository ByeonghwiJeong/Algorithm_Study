"""
https://www.acmicpc.net/problem/21921
제목: 블로그

문제)
- 찬솔이는 블로그를 시작한 지 벌써 N일이 지났다
- X일 동안 가장 많이 들어온 방문자 수와 그 기간들을 구하시오
- 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지


입력)
5 2        : N, X 
1 4 2 5 1  : 5(N)일 동안의 방문자 수
출력)
7          : 가장 많이 들어온 방문자 수 (0이면 전체 SAD 출력)
1          : 가장 많이 들어온 방문자 수가 나온 기간의 수
"""

import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

prefix_sum = [0]
for i in range(N):
    prefix_sum.append(prefix_sum[-1] + visitors[i])

max_visitors = 0
max_visitors_cnt = 0

for i in range(X, N + 1):  # prefix_sum index 1부터 시작
    current_visitors = prefix_sum[i] - prefix_sum[i - X]

    if current_visitors > max_visitors: # 새로운 최대값
        max_visitors = current_visitors
        max_visitors_cnt = 1  
    elif current_visitors == max_visitors:
        max_visitors_cnt += 1

if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(max_visitors_cnt)