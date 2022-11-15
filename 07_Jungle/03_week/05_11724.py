'''
< 연결 요소의 개수 > 
https://www.acmicpc.net/problem/11724
문제 - 연결요소(Connected Component)
양방향
입력)
- 1     : N, M
    N : 정점의 개수 ~ [1 \ 1000]
    M : 간선의 개수 ~ [0 \ N*(N-1)/2]
- 2[M]  : 간선의 양 끝점 u, v
출력)
연결요소의 개수
'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(x):
    global visited
    visited[x] = 1
    for nxt in adj[x]:
        if visited[nxt]: continue
        dfs(nxt)
    return

ans = 0
for i in range(1, n + 1):
    if visited[i]: continue
    ans += 1
    dfs(i)
print(ans)
