'''
0번째가 0 주의 
수열에서 n이 몇부터 시작하는지 항상 체크!!!

'''
import sys
input = sys.stdin.readline

def multi(a, b):
    ans = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            x = 0     
            for k in range(2):
                x += a[i][k] * b[k][j] % 1000000007
            ans[i][j] = x % 1000000007
    return ans

def recur(a, n):
    if n == 1:
        return a
    x = recur(a, n // 2)

    if n % 2:
        return multi(multi(x, x), a)
    else:
        return multi(x, x)

A = [[2, 1], [1, 0]]
M = [[1, 1], [1, 0]] 
# 피보나치 행렬!!!! 
# [[1, 1], [1, 0]] => 활용 은근 많이함
N = int(input())
ans = multi(A, recur(M, N))
print(ans[1][1])

