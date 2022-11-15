'''
< 아침 산책 > 
https://www.acmicpc.net/problem/21606
문제)
- N개의 장소를 N-1개의 길이 잇는 트리형태로 단순화
- 트리구조 : 모든 장소를 몇 개의 길을 통해 갈 수 있음
- 시작점과 도착점을 정함
    - 트리 위에 두 점 사이의 경로는 유일함
- N개의 장소 >>> 실내 or 실외
- 경로 조건
    - 산책의 시작 끝지점 둘다 실내
    - 산책경로에서 시작 끝을 제외하고는 실외
- 서로 다른 산책 경로수
입력)
- 1     : 정점의 수 N
- 2     : 1과0으로 이루어진 문자열 A
    - i번째 문자 Ai가 1인경우 실내
    - 0인경우 실외
- 3[N-1]: 3 ~ N+1번줄 \
    - i+2번줄 트리의 각 간선을 나타내는 두 정수 u, v
    - i번째 간산이 u번 정점과 v번 정점을 연결한다.   
출력)
'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
s = [0] + list(map(int, input().rstrip()))
adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(x):
    global cnt
    visited[x] = 1
    for nxt in adj[x]:
        if visited[nxt]: continue
        if s[nxt]:
            cnt += 1
            visited[nxt] = 1
            continue
        dfs(nxt)
    return

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    if not s[i]: continue 
    dfs(i)
    
print(cnt)
'''
60점
'''