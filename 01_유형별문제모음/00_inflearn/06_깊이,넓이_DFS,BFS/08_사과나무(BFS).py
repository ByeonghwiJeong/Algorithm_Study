'''
N x N [N은 홀수]

다이아몬드 모양으로 수확을할때 그합은?(BFS방식으로 구현)

'''
from collections import deque

N = int(input())
_list = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
sum = 0

dc = (1, 0, -1, 0)
dr = (0, 1, 0, -1)


def bfs():
    global sum
    s = N // 2
    start = (s, s, 0)
    end_level = s
    visited[s][s] = True
    q = deque()
    q.append(start)
    sum += _list[s][s]
    while q:
        r, c, l = q.popleft()
        if l == end_level:
            break
        nl = l + 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not visited[nr][nc]:
                q.append((nr, nc, nl))
                sum += _list[nr][nc]
                visited[nr][nc] = True

bfs()
print(sum)

'''
사각형 가운데 (N//2, N//2)를 기준으로 커지면서 지속적으로 더하며
특정 레벨 N//2에 도달했을때 함수를 break시킨다.

개인적으로 시작 level을 0으로 할지 1으로할지 혼돈이왔다.
깔끔하게 l이 N//2일때 break하기위해서 시작을 0으로했다
'''