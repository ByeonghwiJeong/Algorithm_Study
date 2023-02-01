'''
< Tree >
https://www.acmicpc.net/problem/13244
문제)
- 트리의 특징
    1. 연결됨 : 모든 정점에서 다른 모든 정점으로 경로가 존재
    2. 간선 삭제시 : 연결되지 않음,
        - 특정 노드에서 모든 노드로 도달할 수 없음
    3. 간선 추가시 : Cycle이 생김
- 그래프가 트리인지 아닌지 판별
입력)
- 1     : 그래프 수 T (1 <= T <= 10)
- 2     : 정점 수 N (1 <= N <= 1000)
- 3     : 간선 수 M (1 <= M <= 10^6)
- 4[M]  : 간선 정보 (u, v) (1 <= u, v <= N) 
    - 양방향
출력)
- 1     : 트리면 "tree", 아니면 "graph"
'''
import sys
input = sys.stdin.readline

def dfs(x):
    global visited, graph
    visited[x] = 1
    for nx in graph[x]:
        if visited[nx]: continue
        dfs(nx)
    return

for _ in range(int(input())):
    n = int(input())
    m = int(input())
    visited = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    dfs(1)
    if sum(visited) == n and m == n-1:
        print("tree")
    else:
        print("graph")

'''
- 트리의 특징 : Edge의 개수 = Vertex의 개수 - 1
- dfs로 한번에 모든 정점을 방문!!!
'''