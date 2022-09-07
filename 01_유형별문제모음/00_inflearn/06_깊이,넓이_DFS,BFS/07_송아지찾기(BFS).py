'''
A와 B의 위치가 직선상의 좌표점으로 주어진다.
A에서 B위치까지 다음과 같은 방법으로 이동한다.

한번의 점프로 
앞1\앞5\뒤1

몇번 점프로 갈 수 있는지
입력)
- 1 : A와 B의 위치 [1 \ 10,000]
출력)
- 1 : 점프의 최소횟수를 구한다.
'''
from collections import deque


s, e = map(int, input().split())
move = [-1, 1, 5]
visited = [False] * 10010

def bfs(x):
    global visited, e
    visited[x] = True
    q = deque()
    q.append((x, 0))
    while q:
        a, d = q.popleft()
        if a == e:
            return d
        for m in move:
            na = a + m
            if 1 <= na <= 1001:
                if not visited[na]:
                    visited[na] = True
                    q.append((na, d + 1))
                
print(bfs(s))

