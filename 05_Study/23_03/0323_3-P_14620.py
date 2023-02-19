'''
< 꽃길 >
https://www.acmicpc.net/problem/14620
문제)
- N x N 화단에 꽃씨앗 3개를 심는다. 
- 씨앗을 중심으로 4방향으로 만개한다.
- 서로 꽃잎이 닿는경우 모두 죽어버린다
    - 세 씨앗이 모두 꽃이 피게 해야한다.
- 모두 꽃이 피게하면서 최소 비용을 출력하시오

입력)
- 1     : 화단의 한변의 길이 N ~ [6, 10]
- 2[N]  : N개씩 지점당 가격 ~ [0, 200] 
출력)
- 1     : 최소비용출력
'''
import sys
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
ret = 987654321
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def setFlower(r, c):
    visited[r][c] = 1
    costs = a[r][c]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        visited[nr][nc] = 1
        costs += a[nr][nc]
    return costs

def erasesFlower(r, c):
    visited[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        visited[nr][nc] = 0

def check(r, c):
    if visited[r][c]: return 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < N and 0 <= nc < N): return 0
        if visited[nr][nc]: return 0
    return 1

def dfs(cnt, cost):
    global ret
    if cnt == 3:
        ret = min(ret, cost)
        return
    for i in range(N):
        for j in range(N):
            if check(i, j):
                dfs(cnt + 1, cost + setFlower(i, j))
                erasesFlower(i, j)


dfs(0, 0)
print(ret)

'''
### 완전탐색
10 x 10 격자무늬에서 
100C3 < 100^3 = 100만 < 1억 : 완탐가능
### 기본 로직
```python
visited[ny][nx] = 1
go()
visited[ny][nx] = 0
```
- 1️⃣ 꽃을 심을수 있나??? check함수로 5방향 방문&범위 체크 
- 2️⃣ 꽃방문처리 & 비용산출 setflower 함수
- 3️⃣ 다른꽃심는 재귀함수 
- 4️⃣ 꽃방문 처리 해제

### 조건 체크 순서 주의❗
- 범위안에 있는지 check
- 그 범위에서 방문체크
```python
    if not (0 <= nr < N and 0 <= nc < N): return 0
    if visited[nr][nc]: return 0
```
'''