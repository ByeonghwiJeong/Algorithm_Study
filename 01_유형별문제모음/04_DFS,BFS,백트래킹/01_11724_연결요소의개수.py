'''
- M이 최대 nC2만큼 차지
- DFS나 BFS로 풀수있음
- chk 배열 생성 [][][][][][][]
6 5
1 2
2 5
5 1
3 4
4 6
- 첫번째 체크 후 1번에 연결된것들 연달아 체크
- [1in] 1(+1) > 2 > 5 > 1 [1out] [2 out]
- [3in] 3 > 4 > 6 [3out] [4out] [5out] [6out] 
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
# 문제에서 1 ~ N 으로 간선접점이 주어진다고함
# N(zero base)으로할지 N+1(one base)으로 할지
# N으로 할경우 a와 b에 -1을 해야함
for _ in range(M):
  a, b = map(lambda x: x - 1, map(int, input().split()))
  adj[a][b] = adj[b][a] = 1

ans = 0
chk = [False] * N

def dfs(now):
  for nxt in range(N):
    if adj[now][nxt] and not chk[nxt]:
      chk[nxt] = True
      dfs(nxt)
'''
<check 방법>
1. 방문(dfs호출) 직전에 check하기(추천)
2. dfs호출 직후에 check하는 방식 
'''
for i in range(N):
  if not chk[i]:
    ans += 1
    chk[i] = True
    dfs(i)

print(ans)