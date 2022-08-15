'''
n개의 정수로 이루어진 임의의 수열이 주어진다.
우리는 이 중 연속된 몇개의 수를 선택해서
구할 수 있는 가장 큰 합을 구하려고한다.
10
10  -4   3   1   5   6  -35   12   21   -1
10   6   9   10  15  21  -14 x 12  33   32

10
2   1  -4   3   4  -4   6   5   -5  1
2   3  -1 x 3   7   3   9  14   9  10

연속적으로 합을 하다가 
1. 단독 수
2. 합의 수
1, 2 의 크기를 비교 후 단독이 큰경우 x check

dp 테이블 만들때 사이즈가 매우 중요하다 
0으로 초기화 한경우 min max값에 영향을 줄수 있음

inf 선언시 987654321 

12 15 16

'''
import sys
input = sys.stdin.readline

n = int(input())
_list = list(map(int, input().split()))
dp = [int('-inf')] * (n + 1) 
# dp = [0] * n 
dp[0] = _list[0]
for i in range(1, n):
    dp[i] = max(_list[i], dp[i-1] + _list[i])
# print(dp) 
# -21  -56  -6  -23 0
print(max(dp))