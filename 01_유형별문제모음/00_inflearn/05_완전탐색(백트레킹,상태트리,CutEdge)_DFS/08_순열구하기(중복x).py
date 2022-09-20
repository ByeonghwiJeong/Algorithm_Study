'''
입력)N M 자연수
nPm의 경우 모두 출력
'''
N, M = map(int, input().split())
visited = [0] * (N + 1)
result = []
cnt = 0

def dfs(L):
    global result
    global visited
    global cnt
    if L == M:
        cnt += 1
        print(*result)
        return
    for i in range(1, N+1):
        if not visited[i]:
            result.append(i)
            visited[i] = True
            dfs(L + 1)
            result.pop()
            visited[i] = False
dfs(0)
print(cnt)