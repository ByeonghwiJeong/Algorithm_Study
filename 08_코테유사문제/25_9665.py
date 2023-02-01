'''
실버5
돌 게임
- 돌 N개가 있다. 상근 창영 번갈아가벼 돌을 가져간다.
- 마지막돌을 가져간사람이 이긴다.
- 돌은 1 or 3개 가져갈 수 있다.
- 상근이가 게임 시작
- 상근 Win: "SK" 
- 창영 Win: "CY"
상근    1       1
창영        1
'''
import sys
input = sys.stdin.readline

N = int(input())
# 돌이 N개일때 게임횟수 DP
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = min(dp[i-1], dp[i-3]) + 1

if dp[N] % 2: print("SK")
else: print("CY")