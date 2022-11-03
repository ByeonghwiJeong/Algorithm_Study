'''
https://www.acmicpc.net/problem/9020
< 골드바흐의 추측 >
- 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있음
- 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티쎤은 존재한다.
- n의 골드바흐 파티션을 출력
- n의 골드바흐 파티션이 여러가지인 경우에는 두 소수의 차이가 작은것을 출력
'''
import sys
input = sys.stdin.readline

dp = [1] * 10004
dp[1] = 0
deci = []
for i in range(2, 10001):
    if dp[i]:
        deci.append(i)
        for j in range(i*2, 10001, i):
            dp[j] = 0
for _ in range(int(input())):
    n = int(input())
    l = [0, 0]
    for i in deci:
        if i >= n // 2 + 1:
            break
        if dp[n - i]:
            l[0] = i
            l[1] = n - i
    print(*l, sep=' ')

