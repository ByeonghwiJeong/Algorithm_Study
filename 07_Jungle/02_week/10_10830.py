'''
< 행렬 제곱 >
https://www.acmicpc.net/problem/10830
문제)
- 크기가 N * N인 행렬A
- A의 B제곱
- 각원소를 1000으로 나눈값
입력)
- A, B, C ~ int형 범위 21억
출력)
- 
'''
import sys
input = sys.stdin.readline

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def mult_matrix(a, b):
    l = len(a)
    ret = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                ret[i][j] += a[i][k]*b[k][j]
            ret[i][j] %= 1000
    return ret

def recur(a, n):
    if n == 1: return a
    if n == 2: return mult_matrix(a, a)
    x = recur(a, n //2)
    ret = mult_matrix(x, x)
    if n % 2:
        return mult_matrix(ret, a)
    else: 
        return ret
    
for i in recur(a, b):
    for j in i:
        print(j % 1000, end=' ')
    print()
