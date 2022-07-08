"""
1. 아이디어
- 2중 for, 값 1 && 방문X => DFS
- DFS를 통해 찾은 값을 저장 후 정렬 해서 출력
2. 시간복잡도
- DFS : O(V+E)
- V, E : N^2, 4N^2
- V+E : 5N^2 ~= N^2 ~= 625 >> 가능
3. 자료구조
- 그래프 저장 : int[][]
- 방문여부 : bool[][]
- 결과값 : int[]

문제
https://www.acmicpc.net/problem/2667
"""

import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
# 동 남 서 북  > 동쪽부서 시계 방향
sum = 0

def dfs(y, x):
  global sum
  sum += 1
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0<=ny<N and 0<=nx<N:
      if chk[ny][nx] == False and map[ny][nx]:
        chk[ny][nx] = True
        dfs(ny, nx)
  return sum



sol = []

for j in range(N):
  for i in range(N):
    if map[j][i] == 1 and chk[j][i] == False:
      chk[j][i] = True
      sum = 0
      dfs(j, i)
      sol.append(sum)

sol.sort()
print(len(sol))
for v in sol:
  print(v)
