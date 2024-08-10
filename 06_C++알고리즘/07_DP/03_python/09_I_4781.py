'''
https://www.acmicpc.net/problem/4781
문제 : 사탕가게

- 두 사람이 같은 돈을 가지고 사탕을 산다.
- 이때 구매한 사탕의 칼로리가 더 큰 사람이 이긴다.
- 사탕의 가격과 칼로리가 주어졌을 때, 칼로리의 합이 최대로 하고싶다.

입력)
각 테스트 케이스가 있으며 '0 0.00'이 입력되면 종료

- 1 : n ~ [1, 5000], m ~ [0.01, 100.00]
    - n : 사탕의 종류
    - m : 돈
- 2 ~ n+1 : 사탕의 가격, 칼로리
'''
import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    if n == 0: break

    n = int(n)
    m = int(m * 100 + 0.5) # 부동소수점 오차를 해결하기 위해 정수로 변환

    candies = []
    for _ in range(n):
        c, p = map(float, input().split())
        c = int(c)
        p = int(p * 100 + 0.5)
        candies.append((c, p))

    dp = [0] * (m + 1)

    for i in range(1, m + 1): # 돈 i를 가지고 최대 칼로리를 구한다.
        for c, p in candies: # 사탕의 칼로리, 가격
            if i < p: continue
            dp[i] = max(dp[i], dp[i - p] + c)

    print(dp[m])

