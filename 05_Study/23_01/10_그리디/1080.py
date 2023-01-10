'''
0과 1로만 이루어진 행렬A과 행렬B가 있다.
A를 B로 바꾸는데 필요한 연산횟수의 최소값

행렬을 변환하는 연산 3 x 3 크기의 부분행렬에 있는 모든 원소를 뒤집는것

'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

a = [list(map(int, list(input().rstrip()))) for _ in range(n)]
b = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def change(r, c, matrix):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            matrix[i][j] = 1 - matrix[i][j]
    return

def is_same(n, m, A, B):
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]: return False
    return True

cnt = 0

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            change(i, j, a)
            cnt += 1
#출력
if is_same(n, m, a, b): print(cnt)
else: print(-1)
