'''
< 스타트와 링크 >
- 사람 N명(짝수)
    - 1 ~ N번
- N/2명씩 스타트팀과 링크팀
- i번과 j번사람이 같은 팀에 속했을 때,
    팀에 더해지는 능력치 -> S_ij + S_ji
- 능력치 차이를 최소로 하고싶다.
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
---
1 3 6
1 1
1 3
1 6

->  
2 4 5
'''
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * (n + 1)
min_diff = 987654321

def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1 - power2))
        return

    for i in range(idx, n):
        if visited[i]: continue
        visited[i] = 1
        dfs(depth+1, i+1)
        visited[i] = 0

dfs(0, 0)
print(min_diff)