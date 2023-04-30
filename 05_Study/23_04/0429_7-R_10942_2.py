"""
< 팰린드롬? >
https://www.acmicpc.net/problem/10942
문제)
- 명우, 홍준 팰린드롬 놀이
- 홍준이는 자연수 N개를 칠판에 적음
- 명우에게 질문을 총 M번 한ㄷ.
- 각 질문에는 두 정수 S와 E (1 <= S <= E <= N)
    - S번째 수에서 E번째 까지 팰린드롬인지?
- 
"""
import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if a[i] == a[i+1]: dp[i][i+1] = 1

for interval in range(2, N): # 위에 간격 1인것 해결, 최대 간격 0 ~ N-1
    for st in range(N - interval):
        en = st + interval
        if a[st] == a[en] and dp[st + 1][en - 1]:
            dp[st][en] = 1

print(*dp, sep='\n')

for _ in range(int(input())):
    r, c = map(lambda x: int(x) - 1, input().split())
    print(dp[r][c])