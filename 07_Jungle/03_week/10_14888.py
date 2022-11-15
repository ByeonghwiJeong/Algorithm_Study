'''
< 연산자 끼워넣기 > 
https://www.acmicpc.net/problem/14888
문제) 
- N개의 수로 이루어진 수열 : A1, A2, ..., AN
- 수와 수사이에 연산자가 주어진다 (N-1개)
- 연산자 : 덧셈(+), 뺄셈(-), 곱셈(x), 나눗셈(/)
- 계산은 연산자 우선 순위를 무시
    - 앞에서 부터 진행
입력)
- 1     : 수의 개수 N ~ [2 \ 11]
- 2     : A1, A2, ...,AN ~ [1 \ 100]
- 3     : 덧셈(+), 뺄셈(-), 곱셈(x), 나눗셈(/)의 갯수 ~ 합 N-1
출력)
- 1     : 최댓값
- 2     : 최솟값
'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
_min = 987654321
_max = -987654321

def dfs(x, r, x1, x2, x3, x4):
    global _min, _max
    if x == n:
        _max = max(_max, r)
        _min = min(_min, r)
        return
    if x1 > 0: dfs(x + 1, r + a[x], x1 - 1, x2, x3, x4)
    if x2 > 0: dfs(x + 1, r - a[x], x1, x2 - 1, x3, x4)
    if x3 > 0: dfs(x + 1, r * a[x], x1, x2, x3 - 1, x4)
    if x4 > 0: dfs(x + 1, int(r / a[x]), x1, x2, x3, x4 - 1)

dfs(1, a[0], add, sub, mul, div)
print(_max)
print(_min)