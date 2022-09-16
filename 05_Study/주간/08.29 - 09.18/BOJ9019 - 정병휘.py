'''
< 십진수 >
((d1 × 10 + d2) × 10 + d3) × 10 + d4)

< 4개의 명령어 D, S, L, R >
- D : n * 2 % 10000
- S : n - 1 if n > 0 else 9999
- L : 각자리수 왼쪽으로 회전
- R : 각자리수 오른쪽으로 회전

A에서 B로 변환하기 위한 최소한의 명령어 나열을 출력해라
'''
from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)


def d(n):
    return n * 2 % 10000

def s(n):
    return n - 1 if n > 0 else 9999

def l(n):
    q, r = divmod(n, 1000)
    return r * 10 + q

def r(n):
    q, r = divmod(n, 10)
    return r * 1000 + q

def bfs(start, end):
    visited = [0] * 10000
    visited[start] = 1
    q = deque()
    q.append((start, ""))
    while q:
        start, result = q.popleft()
        if start == end:
            print(result)
            return 
        nd = d(start)
        ns = s(start)
        nl = l(start)
        nr = r(start)
        if not visited[nd]:
            visited[nd] = 1
            q.append((nd, result + "D"))
        if not visited[ns]:
            visited[ns] = 1
            q.append((ns, result + "S"))
        if not visited[nl]:
            visited[nl] = 1
            q.append((nl, result + "L"))
        if not visited[nr]:
            visited[nr] = 1
            q.append((nr, result + "R"))



for _ in range(int(input())):
    A, B = map(int, input().split())
    bfs(A, B)



'''
출력되는 결과는 배열형태로 q안에 튜플로 보내줬지만
배열형태가아닌 string 타입으로 보내줘도 된다

시간초과가 계속떠서 setrecursionlimit을 빼고 pypy로 하니 통과했다
'''
