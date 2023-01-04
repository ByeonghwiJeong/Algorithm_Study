'''
< 골드바흐의 추측 >
- 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.

'''
import sys
input = sys.stdin.readline

dp = [1] * 1000001
dp[0] = 0
dp[1] = 0
for i in range(2, 1000001):
    if not dp[i]: continue
    for j in range(i+i, 1000001, i):
        dp[j] = 0

while True:
    n = int(input())
    if not n: break
    for i in range(2, 500001):
        if not dp[i]: continue
        if not dp[n-i]: continue
        print(f'{n} = {i} + {n-i}')
        break