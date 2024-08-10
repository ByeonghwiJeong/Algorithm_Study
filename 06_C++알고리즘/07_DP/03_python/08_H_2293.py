'''
https://www.acmicpc.net/problem/2293
문제 : 동전 1

- n가지 종류 동전
- 각각의 동전은 무한정 있다.
- 각각의 동전의 가치는 다르다.
- 사용한 동전 구성이 같은데 순서만 다른것은 같은 경우이다
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])