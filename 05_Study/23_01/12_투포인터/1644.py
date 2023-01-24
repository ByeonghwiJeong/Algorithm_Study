'''
< 소수의 연속합 >
https://www.acmicpc.net/problem/1644
문제)
- 하나 이상의 연속된 소수의 합으로 나타낼 수 잇는 자연수들이 있다.
- 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램
'''
import sys
input = sys.stdin.readline

n = int(input())
prime = []

dp = [1] * (n + 1)
dp[0] = dp[1] = 0

for i in range(2, n + 1):
    if dp[i]:
        prime.append(i)
        for j in range(2*i, n + 1, i):
            dp[j] = 0
prime.append(0)

print(prime)
l = 0
r = 0 
size = len(prime) - 1
sum = prime[0]
ans = 0

while (l <= r and r < size):
    if sum == n:
        ans += 1
        sum -= prime[l]
        l += 1
        r += 1
        sum += prime[r]
    elif sum < n:
        r += 1
        sum += prime[r]
    else: 
        sum -= prime[l]
        l += 1
    # print(f"r:{r}, l:{l}, sum:{sum}")

print(ans)
'''
< 같은 위치에서 시작하는 투포인터 >
- 포인터가 소수가 있는 index값을 벗어났을때 
'''