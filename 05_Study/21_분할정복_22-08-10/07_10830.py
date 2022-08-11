'''
N * N 행렬 제곱

n == 2 인 경우 조건은 필요없음
n == 1 인 경우는 a를 리턴해줘야함

< 체크 > 각행렬의 원소는 1 ~ 1000
>>> 1000 일경우 1000으로 나눈 나머지!!!
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def multiply(a, b):
    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            x = 0
            for k in range(N):
                x += a[i][k] * b[k][j]  % 1000
            ans[i][j] = x % 1000
    return ans

def recur(a, n):
    if n == 1:
        return a
  
    x = recur(a, n // 2)
    if n % 2: # 홀수        
        return multiply(multiply(x, x), a)
    else:
        return multiply(x, x)

# 처음에 주어진 원소값이 1000인경우 반례!!!! 1000으로 나눠야함
X = recur(A, B)
for x in X:
    for y in x:
        print(y % 1000, end=' ')
    print()