# adj = [[0] * 13 for _ in range(13)]
# #  ....

# def dfs(now):
#   for nxt in range(13):
#     if adj[now][nxt]:
#       dfs(nxt)

# dfs(0)

'''
from collections import deque

def bfs()
  dq = deque()
  dq.append(0)
  while dq:
      now = dq.popleft()
      for nxt in range(13):
        if adj[now][nxt]:
          dq.apppend(nxt)
      
dfs(
'''