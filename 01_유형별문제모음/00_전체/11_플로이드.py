"""
1. 아이디어
- 모든점 -> 모든점 : 플로이드
- 비용배열 INF 초기화
- 간선의 비용 대입
- 거쳐서 비용 줄어들경우, 갱신(for문 3번)
2. 시간복잡도
- 플로이드 : O(V^3)
- 1e6 > 가능
3. 변수
- 비용 배열, int[][]

<문제>
https://www.acmicpc.net/problem/11404
<핵심코드>
for i in range(1, n+1): rs[i][i]
for in range(m):
  a, b, c = map(int, input().split())
#a 시작 b 끝 c 비용
  rs[a][b] = min(rs[a][b], c)

#최소값으로 갱신
# k 거치는 값 , j 시작, i 끝
for k in range(1, n+1)
  for j in range(1, n+1):
    for i in range(1, n+1):
      if rs[j][i] > rs[j][k] + rs[k][i]:
        rs[j][i] = rs[j][k] + rs[k][i]
"""
import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
rs = [[INF] * (n+1) for  _ in range(n+1)]

for i in range(1, n+1):
  rs[i][i] = 0

for i in range(m):
  a, b, c = map(int, input().split())
  rs[a][b] = min(rs[a][b], c)

for k in range(1, n+1):
  for j in range(1, n+1):
    for i in range(1, n+1):
      if rs[j][i] > rs[j][k] + rs[k][i]:
        rs[j][i] = rs[j][k] + rs[k][i]

for j in range(1, n+1):
  for i in range(1, n+1):
    if rs[j][i] == INF: print(0, end=' ')
    else: print(rs[j][i], end=' ')
  print()