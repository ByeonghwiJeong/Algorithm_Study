'''
N x M 크기의 행렬 A
M x K 크기의 행렬 B

N x K
'''
# 
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

ans = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        x = 0
        for k in range(M):
            x += A[i][k]*B[k][j]
        ans[i][j] = x

for a in ans:
    print(*a, sep=' ')