'''
사이클만들고 그중 최소비용
'''
import sys
input = sys.stdin.readline

_max = 987654321

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
ans = _max

# 현재까지경ㅂ
def dfs(cnt, curr_city, cost):
    global ans
    if cost > ans: return
    if cnt == n - 1:
        # 돌아올수 있는지 확인 (모든 도시방문 후)
        if graph[curr_city][0]: ans = min(ans, cost + graph[curr_city][0])
        return
    
    for next_city in range(n):
        if visited[next_city]: continue
        if not graph[curr_city][next_city]: continue
        visited[next_city] = 1
        dfs(cnt + 1, next_city, cost + graph[curr_city][next_city])
        visited[next_city] = 0
    return

visited[0] = 1
dfs(0, 0, 0)
print(ans)