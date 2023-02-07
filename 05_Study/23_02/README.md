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
2. 누적합 배열에 원소를 넣을때 for문 2회씩 : Index기준
   1. 1 ~ n, 1 ~ m
   2. n+1 ~ 2*n, m+1 ~ 2*m
3. 해쉬맵(dict or map)을 선언 - 파이썬 defaultdict
4. 전구간에서 interval을 기준으로 전구간을 체크해서 dict update
   key : 합
   value : 수
5. 원하는 수 X를 기준으로 결과에
   1. - dict_A[X]
   2. - dict_B[X]
   3. 전구간 for문 += dict_A[X - i] \* dict_B[i]

## ✏️0207. [14469](https://www.acmicpc.net/problem/14469)

- 소를 오름차순 정렬
- for문 반복
  - 소의 이전 끝나는 시간 기준으로 더 큰값 선택
  - 선택값에 걸리는 시간 더하기 : 끝나는 시간

## ✏️07. [](https://www.acmicpc.net/problem/)

## ✏️08. [](https://www.acmicpc.net/problem/)

## ✏️09. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)
