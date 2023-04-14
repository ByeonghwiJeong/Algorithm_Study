"""
< 물통 >
https://www.acmicpc.net/problem/14867
문제)
- 용량 다른 두 개의 빈 물통 A, B
- 물통에 물을 채우고 비우는 일을 반복
- 물통을 원하는 상태가 되도록 만들고자 함
- 물통 이외에는 물의 양을 정확히 잴 수 있는 방법이 없음
- 가능한 작업 : 3종류
    - 1. [F(x) : Fill x] 
        - 물통 x에 물을 가득 채움
    - 2. [E(x) : Empty x]
        - 물통 x를 비움
    - 3. [M(x, y) : Move water from x to y]
        - 물통 x에서 물을 물통 y로 옮김
        - 물통 x가 비거나 물통 y가 가득 찰 때까지
입력)
- 1      : a b c d
        - a : A 물통의 용량 ~ [1 \ 100,000]
        - b : B 물통의 용량 ~ [1 \ 100,000]
        - c : A의 목표 용량 ~ [0 \ a]
        - d : B의 목표 용량 ~ [0 \ b]
"""
import sys
from collections import deque

input = sys.stdin.readline

visited = dict()
a, b, c, d = map(int, input().split())
q = deque()


def go(x, y, d):
    global q
    if visited.get((x, y)):
        return
    visited[(x, y)] = d + 1
    q.append((x, y))


def bfs(x, y):
    global q
    visited[(x, y)] = 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        go(a, y, visited[(x, y)])  # F(A)
        go(x, b, visited[(x, y)])  # F(B)
        go(0, y, visited[(x, y)])  # E(A)
        go(x, 0, visited[(x, y)])  # E(B)
        # M(A, B)
        # A가 비거나 B가 가득 찰 때까지
        go(max(0, x + y - b), min(x + y, b), visited[(x, y)])
        # M(B, A)
        # B가 비거나 A가 가득 찰 때까지
        go(min(x + y, a), max(0, x + y - a), visited[(x, y)])
    if visited.get((c, d)):
        return visited[(c, d)] - 1
    else:
        return -1


print(bfs(0, 0))


"""
이차원 배열을 이용해서 DP 불가능
- 공간복잡도 너무 크다!!!
- 100,000 * 100,000 = 10억
- map을 이용해서 해결
"""
