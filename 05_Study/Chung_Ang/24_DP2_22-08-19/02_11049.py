'''
크기 N x M 인 행렬 A
크기 M x K 인 행렬 B
A와 B를 곱할 때 필요한 곱셈 연산의 수는 총
N x M x K번이다.
행렬 N개를 곱하는데 필요한 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

예)
    - A: 5x3, B: 3x2, C:2x6
    - ABC곱하는경우의수
    - (AB)C : 5x3x2 + 5x2x6
    - A(BC) : 3x2x6 + 5x3x6

0       5x3x2   min(5*3*2 + 5*2*6, 3*2*6 + 5*3*6)  
0       0       3x2x6
0       0       0
                dp[i][j-1]  dp[i+1, j]
    # dp[i][j] = min(\
    #     dp[i][j-1] + matrix[i][0] * matrix[j-1][1] * matrix[j][1],\
    #         dp[i+1][j] + matrix[i][0] * matrix[i+1][0] * matrix[j][1]\
    # )

행렬 N개의 크기가 주어졌을 때, 최소 연산?
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * N for _ in range(N)]
matrix = []
for _ in range(N):
    matrix.append(tuple(map(int, input().split())))
# N = 4
# 0,1  1,2  2,3  3,4 / 0,2  1,3  2,4 / 0,3  1,4 /  0,4
for size in range(1, N): # size
    for start in range(N - size): # size인 그룹의 경우의 수
        end = start + size
        result = float('inf')
        for cut in range(start, end):
            result = min(result, dp[start][cut] + dp[cut + 1][end] +\
                matrix[start][0] * matrix[cut][1] * matrix[end][1])
        dp[start][end] = result

print(dp[0][N-1])