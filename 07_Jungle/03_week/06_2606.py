'''
< 연결 요소의 개수 > 
https://www.acmicpc.net/problem/2606
문제) - 연결요소(Connected Component)
양방향
시작점이 주어졌을때 그 점을 기준으로 \
    Connected Component의 크기
입력)
- 1     : N 컴퓨터의 수 ~ [1 \ 100]
- 2     : M 간선 수
- 3[M]  : u, v 연결된 컴퓨터 번호
출력)
연결요소의 개수
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(x):
    visited[x] = 1
    ret = 1
    for nxt in adj[x]:
        if visited[nxt]: continue
        ret += dfs(nxt)
    return ret

print(dfs(1) - 1)
'''
자기 포함하면 안됨!!!
'''