'''
<뮤탈리스크>
https://www.acmicpc.net/problem/12869
문제 : DP)
- 수빈 : 뮤탈1개, 강호 SCV : N개
- SCV 남아있는 체력이 주어짐
- 뮤탈리스크는 한 번에 세 개의 SCV를 공격
    - 첫번째 SCV : 9
    - 두번째 SCV : 3
    - 세번째 SCV : 1
- 체력 0이하 되면 파괴
- 모두 파괴하기위해 공격해야하는 횟수의 최소값
입력)
- 1     : SCV의 수 N (1 <= N <= 3)
- 2     : SCV N개의 체력 (1 <= 체력 <= 60) 자연수
출력)
-  SCV를 파괴하기 위한 공격 횟수의 최솟값
'''
from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
scv = list(map(int, input().split()))
while len(scv) < 3:
    scv.append(0)
attack = list(permutations([9, 3, 1]))
# 3차원 dp
dp = [[[0] * 64 for _ in range(64)] for _ in range(64)]

def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    while q:
        x, y, z = q.popleft()
        if x <= 0 and y <= 0 and z <= 0:
            return dp[x][y][z]
        for a, b, c in attack:
            # 0 이하면 그냥 유지 음수가 되면 indexError방지
            nx = max(0, x - a)
            ny = max(0, y - b)
            nz = max(0, z - c)
            if dp[nx][ny][nz]: continue
            dp[nx][ny][nz] = dp[x][y][z] + 1
            q.append((nx, ny, nz))
            
print(bfs(*scv))

'''
최단거리 ??? BFS - while & Queue
3차원 배열 DP : 최소횟수 MEMO


'''