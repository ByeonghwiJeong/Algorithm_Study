'''
메모리 & 시간 초과 발생 >>> bfs로 시도
'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
dp = [0] * (n + 1)
# 연결리스트 만들기 b번 > a번 (단방향)
for _ in range(m): 
    a, b = map(int, input().split())
    adj[b].append(a)

def dfs(now):
    visited[now] = 1;
    ret = 1
    for nxt in adj[now]:
        if visited[nxt]: continue
        ret += dfs(nxt)
    return ret

ans = 0
# 모든경우
for i in range(1, n + 1):
    visited = [0] * 10001
    temp = dfs(i)
    if ans < temp:
        ans = temp
        l = []
        l.append(i)
    elif ans == temp: l.append(i)
print(*sorted(l))
# for i, v in enumerate(dp):
#     if ans == v: print(i, end=" ")
