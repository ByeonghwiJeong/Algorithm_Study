'''
< 스타트와 링크 >
https://www.acmicpc.net/problem/14889
문제)
- 짝수 N명을 N/2로 나누어 두 팀으로 나누기
- 사람에게 번호 1 ~ N까지 배정
- 능력치 Sij : i번 사람과 j번 사람이 같은 팀에 속했을 때 능력치
- 두 팀의 능력치 차이의 최솟값
입력)
- 1       : 사람 수 N (4 <= N <= 20)
- 2[N][N] : 능력치 Sij
'''
import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * (N + 1)

ret = 1e9
def dfs(x, idx):
    global ret
    if x == N // 2:
        A, B = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += S[i][j]
                elif not visited[i] and not visited[j]:
                    B += S[i][j]
        ret = min(ret, abs(A - B))
        return
    
    for i in range(idx, N):
        if visited[i]: continue
        visited[i] = 1
        dfs(x + 1, i + 1)
        visited[i] = 0

dfs(0, 0)
print(ret)
