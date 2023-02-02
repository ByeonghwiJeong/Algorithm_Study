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

## ✏️05. [](https://www.acmicpc.net/problem/)

## ✏️06. [](https://www.acmicpc.net/problem/)

## ✏️07. [](https://www.acmicpc.net/problem/)

## ✏️08. [](https://www.acmicpc.net/problem/)

## ✏️09. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)
