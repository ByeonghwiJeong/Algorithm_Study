'''
< 동전 >
https://www.acmicpc.net/problem/9084
문제)
- 동전 1원, 5원, 10원, 50원, 100원, 500원
- 금액이 주어졌을 때 금액을 만드는 모든 방법
1
5 - 5 or 1*5 >> 1 + 1
10 - 10 or (5 * 2 or 1 * 5 + 5 or 1 * 10) >> 1 + 3
50 - 
입력)
- 1     : 테스크 케이스 개수 T ~ [1 \ 10]
- t1    : 동전의 가지수 N ~ [1 \ 20]
- t2    : N가지 동전의 각 금액이 오름차순으로 정렬
- t3    : N가지 동전으로 만들어야 할 금액 ~ [1 \ 10000] 
'''

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    t = int(input())
    dp = [0] * (t + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, t + 1):
            if i < coin: continue
            dp[i] += dp[i - coin]
    print(dp[t])