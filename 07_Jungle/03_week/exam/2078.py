'''
< 무한이진트리 > 
https://www.acmicpc.net/problem/1388
문제
- 무한한 크기의 이진트리 
1. 루트에는 (1, 1)이 할당
2. (a, b)노드에 왼쪽자식: (a+b, b), 오른쪽자식: (a, a+b)
- 어떤 노드 ~ 루트 최단경로를 찾으려한다.
    - 왼쪽 자식으로 이동하는 회수??
    - 오른쪽 자식으로 이동하는회수??
(1, 1)
(2, 1) | (1, 2)
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
lcnt = 0
rcnt = 0
def recur(x, y):
    global lcnt, rcnt
    if x == 1 or y == 1:
        if x > y: lcnt += x - y
        if x < y: rcnt += y - x
        return
    if x > y:
        lcnt += x // y
        recur(x%y, y)
    if x < y:
        rcnt += y // x
        recur(x, y%x)
    return

recur(a, b)
print(lcnt, rcnt)
