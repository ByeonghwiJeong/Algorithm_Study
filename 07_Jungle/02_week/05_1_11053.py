'''
< 가장 긴 증가하는 부분 수열 - O(N^2)>
https://www.acmicpc.net/problem/11053
문제)
-  A = {10, 20, 10, 30, 20, 50}
- 부분수열 = {10, 20, 30, 50}
입력)
- 1     : 수열의 크기
- 2     : 

출력)
- 
'''
import sys
input = sys.stdin.readline
n = int(input())
a = [0]
a += list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1): # 1 ~ N
    for j in range(i): # 0 ~ i-1
        # dp[i]는 A[i]보다 작은 A[j] 중 가장 큰 dp[j]값에 1을 더한값
        if a[i] > a[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))

