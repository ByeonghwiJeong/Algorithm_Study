'''
https://www.acmicpc.net/problem/22954
제목: 그래프 트리 분할

문제
- 정점 N개, 간선 M개의 그래프
- 각 정점은 1부터 N까지 번호가 붙어있음
- 간선도 입력순서대로 1부터 M까지 번호가 붙어있음
- 그래프에서 원하는 만큼 간선을 삭제해, 사로 다른 크기의 트리 2개로 분할해보자
- 각각 트리는 하나 이상의 정점을 가지고 있어야함
- 두 트리가 동일한 정점이나 간선을 공유해서는 안됨

입력
- 1 : 정점의 개수 N~[1 \ 100_000], 간선의 개수 M~[1 \ 200_000]
- 2 : [M lines] 간선을 나타내는 정수 u, v 가 주어짐 ~ [1 \ N], u != v
    - u정점과 v정점을 연결하는 간선이 존재함을 의미 (양방향)
    - 중복된 간선은 없음
```
5 5
1 2
1 3
2 3
3 4
4 5
```
출력
- 그래프를 분할 할 수 없는경우 첫번째 줄에 -1 출력
- 그래프를 분할 할 수 있는 경우

- 1 : 두 트리의 크기 N1, N2 출력 (N = N1 + N2)
- 2 : 첫 번째 트리에 속한 정점 N1개의 번호 출력
- 3 : 첫 번째 트리에 속한 간선 N1-1개의 번호 출력
- 4 : 두 번째 트리에 속한 정점 N2개의 번호 출력
- 5 : 두 번째 트리에 속한 간선 N2-1개의 번호 출력

```
3 2
1 2 3
1 2
4 5
5
```
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

# 그래프 생성
edges = [(0, 0)] # 0번째 인덱스는 사용하지 않음
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))
    graph[u].append((v, i+1))
    graph[v].append((u, i+1))

visited = [0] * (N+1)
components = [] 
current_component = []  

# DFS : Connected Component 찾기
def dfs(node):
    visited[node] = 1
    current_component.append(node)
    for next_node, _ in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

# 모든 정점에 대해 DFS
for i in range(1, N+1):
    if not visited[i]:
        current_component = []
        dfs(i)
        components.append(current_component)

# 