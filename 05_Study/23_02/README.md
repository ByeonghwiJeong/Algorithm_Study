## ✏️0201. [12869](https://www.acmicpc.net/problem/12869)

`BFS` : 3차원 DP배열에서 visited check && memoization

- dp[x][y][z]
- 0이하일 때 IndexError방지를 위해서 `max(0, x-a)`

## ✏️0201. [13244](https://www.acmicpc.net/problem/13244)

-

## ✏️0202. [17143](https://www.acmicpc.net/problem/17143)

## ✏️0202. [13913](https://www.acmicpc.net/problem/13913)

**⭐️⭐️시간 초과 코드⭐️⭐️⭐️**
▶️ 해결법!!!: prev배열을 생성해서 역으로 찾아간다.

```python
from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
visited = [0] * 100001

def bfs(s):
    visited[s] = 1
    q = deque()
    q.append((s, 0, str(s)))
    while q:
        x, t, s = q.popleft()
        if x == K:
            return [t, s]
        nt = t + 1
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= 100000:
                if not visited[nx]:
                    q.append((nx, nt, s + ' ' + str(nx)))
                    visited[nx] = 1

print(*bfs(N), sep='\n')
```

### ⭐️⭐️⭐️이동 경로가 출력방법 prev ⭐️⭐️⭐️

`1 => 4 => 9 => 11`

- prev[11] = 9
- prev[9] = 4
- prev[4] = 1

## ✏️0207. [2632](https://www.acmicpc.net/problem/2632)

### ⭐️원형 고리 구조!!!⭐️ (시작과 끝이 이어짐)

- 선형적인 자료구조를 두개 이어붙이자!
- 누적합도 원형구조를 고려해서 계산

### <풀이법>

1. A, B 각각의 조각에 있어서 누적합배열 psum_A, psum_B을 정의
   - 초기값 [0]
2. 누적합 배열에 원소를 넣을때 for문 2회씩 : **Index기준**
   1. `1 ~ n`, `1 ~ m`
   2. `n+1 ~ 2*n`, `m+1 ~ 2*m`
3. 해쉬맵(dict or map)을 선언 - 파이썬 **defaultdict**
4. 전구간에서 interval을 기준으로 전구간을 체크해서 dict update
   - `key` : 합
   - `value` : 수
5. 원하는 수 X를 기준으로 결과에
   1. - dict_A[X]
   2. - dict_B[X]
   3. 전구간 for문 += dict_A[X - i] \* dict_B[i]

## ✏️0207. [14469](https://www.acmicpc.net/problem/14469)

- 소를 오름차순 정렬
- for문 반복
  - 소의 이전 끝나는 시간 기준으로 더 큰값 선택
  - 선택값에 걸리는 시간 더하기 : 끝나는 시간

## ✏️0208. [1189](https://www.acmicpc.net/problem/1189)

### 재귀함수(r, c)

- 목표 위치 도달
  - 조건❌ : return 1
  - 조건⭕️ : return 0
- ret = 0 선언
- 4방향 탐색
  - 여러 조건 확인
  - 방문체크
  - ret += 재귀함수(nr, nc)
  - 방문해제
- return ret

## ✏️0208. [5430](https://www.acmicpc.net/problem/5430)

1. string 배열을 진짜 배열로 만들기
   - 예외case: '[]'
2. 직접 뒤집으면 안된다 - 시간초과 방지
   - 방향 boolean상수 `direction`선언

## ✏️0209. [17298](https://www.acmicpc.net/problem/17298)

### 스택 자료구조 활용

- for 1 ~ N:
  - while :스택에 자료가 있고 \ 값[스택top]보다 오른쪽수가 더 크면
    - ans[스택top] = 오른쪽수
    - 스택pop
  - index를 스택에 넣기

## ✏️0209. [1781](https://www.acmicpc.net/problem/1781)

### 1. 라인스위핑

- 문제에는 데드라인이 있음 - 구간안에 풀어야함!!!
- ![라인스위핑](https://blog.kakaocdn.net/dn/biuYDc/btrrpEpHCiq/iOCbtB5hkcYMmtt9NEqwW0/img.png)

### 2. 배치 고려 - 정렬

- ![정렬](https://user-images.githubusercontent.com/95831345/217975364-de64b08d-7ec9-4e86-be34-75b2e778c2e2.png)
- 정렬기준 : 데드라인

### 로직

1. 데드라인기준 정렬
2. ret = 0, hq = [] 선언
3. for문 1 ~ N-1
   1. ret 에 index컵라면 더하기
   2. hq의 크기(걸리는시간) > index데드라인 - 데드라인넘는경우
      - ret에 hq의 최소값빼기(최소힙 pop) - 최소컵라면빼기
4. ret 출력

## ✏️0210. [12100](https://www.acmicpc.net/problem/12100)

### 4방향의 로직구현이 XX

- 1. 1방향로직
  - 일차원 배열에서 같은것 합치기 왼쪽으로 밀기
- 2. 90도 rotate (암기)

```python
# 90도 회전
def rotate(B):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = B[N - 1 - j][i]
    return tmp
```

## ✏️0210. [15926](https://www.acmicpc.net/problem/15926)

### 로직1

![참고](https://user-images.githubusercontent.com/95831345/217994184-2cf43402-7f80-47d0-b2a8-3cf1680e193e.png)

- **단순**
- 유효한 괄호 부분을 1로 표시하는방법
  - 최종적으로는 한번 연속된 1은 숫자롤 올려준다.
- **로직**
- 스택활용 : for문 i : 0 ~ n-1
  - 정방향괄호 : '(' 이면 i-push
  - 반대방향괄호 :
    - stk에 잇는 경우
      - 그 i부분 1 stk top도 1 저장
      - d[i]=d[stk.pop()]=1
    - stk에 원소 없는 경우루
      - continue

### 로직2

1. stk에 [-1]로 선언
2. for문 i ~ [1 \ n-1]
   1. s[i]가 '('이면 stk에 i push
   2. s[i]가 ')'이면
      - stk.pop() 원소 빼기
      - 스택에 원소 있으면
        - ret = max(ret, i - stk[-1])
      - 스택에 원소 없으면
        - stk.append(i)

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

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)
