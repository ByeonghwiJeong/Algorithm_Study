## ✏️0320. [11723](https://www.acmicpc.net/problem/11723)

### ⭐⭐⭐`비트 마스킹`⭐⭐⭐

공집합에 x를 추가
=> x번째에 1을 or연산자로 추가
=> n의 범위가 최대 20 (n이 30이하이므로 비트마스킹 적용가능)

<img width="600" alt="image" src="https://user-images.githubusercontent.com/95831345/227275512-ee68412c-cda2-4499-b4b2-3779b6b99213.png">

### `add` : x번째 비트 ON

- `n |= (1 << x)`
- OR연산자는 이미 있는경우는 무시

### `remove` : x번째 비트 OFF

- `n &= ~(1 << x)`

### `check` : x번째 비트 확인

- `if(n & (1 << x))`
- python 삼항 연산자
  - 참인경우 if 조건 else 거짓인경우

### `toggle` : x번째 비트 XOR연산

- 0은 1, 1은 0
  - x가 있으면 x를 제거, 없으면 x를 추가
- `n ^= (1 << x)`

### `all` : 크기가 21인 집합의 모든 비트를 켜기

- 1 ~ 20 표현하기위해서 크기 21
- `(1 << 21) - 1`

### `empty` : 공집합으로 만들기

- n = 0

## ✏️0320. [5719](https://www.acmicpc.net/problem/5719)

- 최단거리 간선 제거 `-1`으로 표기

### 다익스트라

```python
def dijkstra():
    distance = [INF] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, S))
    distance[S] = 0
    while pq:
        cost, now = heapq.heappop(pq)
        if distance[now] < cost: continue
        for i, nxt in enumerate(a[now]):
            if nxt == -1: continue
            next_cost = cost + nxt
            if distance[i] > next_cost:
                distance[i] = next_cost
                heapq.heappush(pq, (next_cost, i))
    return distance
```

## ✏️0321. [14502](https://www.acmicpc.net/problem/14502)

### dfs구현문제 : 바이러스확산을 막기위한 벽세우기 문제

1. 빈칸을 미리 체크하기
   - 모든경우의수 체크(효율적으로 벽세우기 X)
2. 빈칸중에서 3개를 뽑아서 벽으로 체크하기
   - 바이러스 확산 시키기
   - 확산이후에 빈칸 갯수 세기(return)
3. 최대 값이면 갱신

## ✏️0322. [16434](https://www.acmicpc.net/problem/16434)

1. 이분탐색 풀이
2. 그리디 풀이

## ✏️0323. [14620](https://www.acmicpc.net/problem/14620)

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

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)
