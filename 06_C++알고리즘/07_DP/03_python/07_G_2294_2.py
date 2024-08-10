'''
https://www.acmicpc.net/problem/2294
문제 : 동전 2

- n가지 종류 동전
- 동전을 조합해서 k원을 만들려고 한다.
- 동전의 최소 개수를 구하라.
- 가치가 같은 동전이 여러 번 주어질 수도 있다

입력)
- 1 : n ~ [1, 100], k ~ [1, 10000]
- 2 ~ n+1 : 각 동전의 가치
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [-1] * (k + 1)
dp[0] = 0  # 0원을 만드는 데 필요한 동전 개수는 0

for coin in coins:
    # 현재 동전부터 목표 금액까지
    for i in range(coin, k + 1):
        if dp[i - coin] == -1: continue
        if dp[i] == -1:
            dp[i] = dp[i - coin] + 1
        else:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k])