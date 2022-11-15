'''
< 트리의 부모 찾기 > 
https://www.acmicpc.net/problem/11725
문제) 
- 루트 없는 트리가 주어진다.
- 트리의 루트를 1이라고 했을때 \
    각 노드의 부모를 구하시오
입력)
- 1     : 노드의 개수 N ~ [2 \ 100,000]
- 2[N-1]: 트리상 연결된 두 정점
출력)
'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(x):
    global visited
    for nxt in adj[x]:
        if visited[nxt]: continue
        visited[nxt] = x
        dfs(nxt)
    return

visited[1] = 1
dfs(1)
print(*visited[2:], sep='\n')
