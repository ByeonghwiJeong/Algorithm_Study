"""
< 소수의 연속합 >
https://www.acmicpc.net/problem/1644
문제)
- 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다.
- 3     : 
"""
import sys

input = sys.stdin.readline

N = int(input())
prime = []
dp = [1] * (N + 1)
dp[0] = 0
dp[1] = 0

for i in range(2, N + 1):
    if dp[i]:
        prime.append(i)
        for j in range(i * 2, N + 1, i):
            dp[j] = 0
prime.append(0)

l = 0
r = 0
size = len(prime) - 1  # 위에 prime.append(0) 때문에
ans = 0
sum = prime[0]

while l <= r:
    if r >= size:
        break
    if sum == N:
        ans += 1
        sum -= prime[l]
        l += 1
        r += 1
        sum += prime[r]
    elif sum < N:
        r += 1
        sum += prime[r]
    else:
        sum -= prime[l]
        l += 1
    # print(f"r:{r}, l:{l}, sum:{sum}")
print(ans)
