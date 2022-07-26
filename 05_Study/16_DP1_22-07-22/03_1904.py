'''
2진 타일
1 00 타일 만 존재 > 01 10 xxx
N = 1 : 1
N = 2 : 00 11
N = 3 : 001 / 111 / 100 
N = 4 : 0011 / 1111 / 1001 / 0000 / 1100
n3 = n2 + n1

주의 주의 dp 생성시 N + 1 아 아닌 범위로 하는것 추천
N이 작을때 index error
'''
import sys
input = sys.stdin.readline

N = int(input())
# dp = [0] * (N + 1) index error 발생
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= 15746
print(dp[N])