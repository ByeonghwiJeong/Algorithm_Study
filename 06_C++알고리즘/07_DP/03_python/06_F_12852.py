'''
https://www.acmicpc.net/problem/12852
문제 : 1로 만들기 2

정수 X에 사용할 수 있는 연산은 세가지
- X가 3으로 나누어 떨어지면, 3으로 나눈다.
- X가 2로 나누어 떨어지면, 2로 나눈다.
- 1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하라.

입력)
- 1 : N ~ [1, 1000000]
- 2 : N이 1이 될 때가지 그 수를 공백으로 구분하여 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1) 
# dp[i] : i를 1로 만들기 위한 최소 연산 횟수
prev = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1 # 1을 빼는 경우
    prev[i] = i - 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1: 
        # 2로 나누는 경우 
        dp[i] = dp[i // 2] + 1
        prev[i] = i // 2

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        # 3으로 나누는 경우
        dp[i] = dp[i // 3] + 1
        prev[i] = i // 3

print(dp[N])

while N != 0:
    print(N, end=' ')
    N = prev[N]

