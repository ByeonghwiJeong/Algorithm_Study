'''
메모리 & 시간 초과 발생 >>> bfs로 시도
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
dp = [0] * (n + 1)
# 연결리스트 만들기 b번 > a번 (단방향)
for _ in range(m): 
    a, b = map(int, input().split())
    adj[b].append(a)

# def bfs(now):
#     visited[now] = 1;
#     ret = 1
#     q = deque([now])
#     while q:
#         here = q.popleft()
#         for nxt in adj[here]:
#             if visited[nxt]: continue
#             visited[nxt] = 1
#             ret += 1
#             q.append(nxt)
#     return ret

ans = 0
# 모든경우
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    # temp = bfs(i)
    visited[i] = 1
    ret = 1
    q = deque([i])
    while q:
        here = q.popleft()
        for nxt in adj[here]:
            if visited[nxt]: continue
            visited[nxt] = 1
            ret += 1
            q.append(nxt)
    if ans < ret:
        ans = ret
        l = []
        l.append(i)
    elif ans == ret: l.append(i)
print(*sorted(l))
# for i, v in enumerate(dp):
#     if ans == v: print(i, end=" ")
