# [IT기업 및 대기업 계열사 유사 문제 모음](https://www.acmicpc.net/workbook/view/8708)

---

## ✏️01. [1238](https://www.acmicpc.net/problem/1238)

- ❗️**일반적인 다익스트라**
  - dist INF 배열 생성후 최소 Cost check
  - heap자료구조 사용
- 왕복이므로 각 위치마다 다익스트라 함수 2번 호출

## ✏️02. [13549](https://www.acmicpc.net/problem/13549)

- heap을 사용한 BFS
- ❗️**처음 if문에서 무분별한 continue 사용**
  - 첫번째 2\*x이동조건에서 다른 while문으로 넘겨버림

## ✏️03. [4485](https://www.acmicpc.net/problem/4485)

- ❗️**일반적인 다익스트라**
- heap 자료 구조 사용
- dijkstra 기본 : INF를 요소로 가지는 배열 생성
- 4방향 탐색후 이전 값보다 현재값이 작은 경우 갱신

## ✏️04. [1253](https://www.acmicpc.net/problem/1253)

- ❗️<span style="color:red">전형적인 </span>⭐️⭐️**투 포인터 Two-Pointer**⭐️⭐️
- **<4가지 주의사항>**
  1. 입력 받은 숫자들을 정렬했는가?
  2. 숫자 목록에 음수가 포함
  3. 수의 위치가 다르면 값이 같아도 다른 수라는 조건 고려
  4. 투포인터로 검사할 때 현재 검사하고자 하는 숫자는 제외했는가?
-

## ✏️05. [1806](https://www.acmicpc.net/problem/1806)

- ❗️누적합 PrefixSum : 초기값 0
- 1️⃣**PrefixSum**
  - 왼쪽부터 시작 : st=0, en=1
  - while문 조건 : st < n
    - 조건만족시 st증가
    - 조건불만족시 en을 먼저 계속 증가

```python
    while st < n: # st < en ❌
        S = prefix_sum[en] - prefix_sum[st]
        # S가 target보다 클때 point 좁히기
        if S >= target:
            ans = min(ans, en - st)
            st += 1
        else:
            if en < n: en += 1 # 합을 크기 만들기 위해서
            else: st += 1 # 탈출 조건을 위해서
```

- 2️⃣**TwoPointer**

```python
def two_pointer(target):
    global ans
    st, en, cur = 0, 0, 0 # 왼쪽부터 시작
    while True:
        if cur >= s:
            ans = min(ans, en - st)
            cur -= a[st]
            st += 1
        elif en == n:
            break
        else:
            cur += a[en]
            en += 1
    return ans
```

## ✏️06. [12919](https://www.acmicpc.net/problem/12919)

- 단순한 dfs문제로 생각했음
- **초기 풀이 - 시간초과발생**
  > 50^2 : 시간 초과발생

```python
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

def dfs(x):
    if x == t:
        print(1)
        sys.exit()
    if len(x) > len(t): return
    dfs(x + 'A')
    dfs((x+'B')[::-1])

dfs(s)
print(0)
```

- ⭐️⭐️**접근 방법 : 반대로 생각하기**⭐️⭐️
  > S ▶️ T가아닌
  > T ▶️ S로 조건에따라서 체크한다

## ✏️07. [14658](https://www.acmicpc.net/problem/14658)

- 완전 탐색은 시간초과가 뜸
- 트램펄린에서 이웃한 모서리에 두개의 별(a, b)이 걸쳐지게 하는 방식으로 탐색
- ⭐️⭐️⭐️⭐️⭐️
- [참고링크](https://astrid-dm.tistory.com/463)

## ✏️08. [2531](https://www.acmicpc.net/problem/2531)

- 슬라이딩 윈도우
- defaultdict 사용

## ✏️09. [22233](https://www.acmicpc.net/problem/22233)

- 기본적인 해쉬맵

## ✏️10. [1987](https://www.acmicpc.net/problem/1987)

- **초기 풀이 - 접근 방식 틀림**

```python
from collections import deque
import sys
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

R, C = map(int, input().split())

a = [input().rstrip() for _ in range(R)]
visited = [[0] * C for _ in range(R)]
alpha = set()

def dfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    alpha.add(a[0][0])
    ans = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if a[nr][nc] in alpha: continue
                if visited[nr][nc]: continue
                q.append((nr, nc))
                visited[nr][nc] = 1
                alpha.add(a[nr][nc])
                ans += 1
    return ans
print(*visited, sep='\n')
print(dfs())
```

- ❗️**최대 몇칸을 이동할 수 있는가?????**
- **두번째 풀이 - 시간초과**
  ▶️ 그냥 pypy로 제출

```python
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

R, C = map(int, input().split())

a = [input().rstrip() for _ in range(R)]
visited = [[0] * C for _ in range(R)]

result = 0

def dfs(r, c, s):
    global result
    result = max(result, len(s))
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if not a[nr][nc] in s:
                dfs(nr, nc, s + a[nr][nc])

dfs(0, 0, a[0][0])
print(result)
```

## ✏️11. [20055](https://www.acmicpc.net/problem/20055)

- **빡 구현 문제**

## ✏️12. [2206](https://www.acmicpc.net/problem/2206)

- 벽부시기 아이디어 : visited 3차원 배열

## ✏️13. [1522](https://www.acmicpc.net/problem/1522)

- **브루트포스인 이유** : 'a'가 연속되어 나타낼 수 있는 모든 경우를 모두 탐색
- 그 중 가장 최소 교환 횟수
- 연속된 'a'인 문자열의 경우를 슬라이딩 윈도우를 통해 하나씩 탐색
- 답이 될 수 있는 문자열을 만든 후, 처음 입력값과 비교

```python
abababababababa
aaaaaaaabbbbbbb 4
baaaaaaaabbbbbb 4
bbaaaaaaaabbbbb 4
bbbaaaaaaaabbbb 4
bbbbaaaaaaaabbb 4
bbbbbaaaaaaaabb 4
bbbbbbaaaaaaaab 4
bbbbbbbaaaaaaaa 4
abbbbbbbaaaaaaa 3
aabbbbbbbaaaaaa 4
aaabbbbbbbaaaaa 3
aaaabbbbbbbaaaa 4
aaaaabbbbbbbaaa 3
aaaaaabbbbbbbaa 4
aaaaaaabbbbbbba 3
3
```

## ✏️14. [20437](https://www.acmicpc.net/problem/20437)

## ✏️15. [16234](https://www.acmicpc.net/problem/16234)

- **첫번째 15점 풀이**

```python
import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
# 오른쪽 지우기
if s[-1] == 'R':
    s = s.rstrip('R')
    a = s.count('R')
    # b = s.count('B')
else:
    s = s.rstrip('B')
    a = s.count('R')
    # b = s.count('B')
print(min(a, len(s)-a))
```

- 오른쪽으로 넘기는 경우말고 왼쪽으로 넘기는 경우도 Check

## ✏️16. [16234](https://www.acmicpc.net/problem/16234)

- **그냥 미쳤네**
  > r, c같은거 상수로 선언하지말자(초기값)

## ✏️17. [14719](https://www.acmicpc.net/problem/14719)

- 양끝을 제외하고 index : 1 ~ W-1
- 한 Column기준으로 양끝 max높이중 작은값 선택
- 현재 index의 높이를 차감해서 물 높이 ans에 더하기

## ✏️18. [2493](https://www.acmicpc.net/problem/2493)

- 스택 + dp문제
- 출력을 등수를 해야하는데
  - stack에는 index를 저장하면서 pop을 반복하고
  - 최종적으로 출력해야하는 dp에 **stack[-1] + 1**

## ✏️19. [5972](https://www.acmicpc.net/problem/5972)

- 전형적인 다익스트라 문제 ( + heapq )
  1️⃣ 탐색 시작노드는 0 나머지는 INF로 초기화한 **distance배열** 선언
  2️⃣ **최소힙**에 (0, 시작노드) 삽입 ~ (비용, 위치)
  ❗️ **반복!!!! while**
  3️⃣ 최소힙에서 원소 꺼내기 : 꺼낸 비용 vs distance[꺼낸 위치]
  -> 꺼낸 비용이 더 크면 pass(continue)
  4️⃣ 위조건을 통과 후 graph[꺼낸 위치]에 저장된 (위치, 비용) Check
  5️⃣ 다음 비용 = 꺼낸비용 + graph비용
  6️⃣ **if** 다음비용이 distance배열[graph 위치] 보다 작은경우
  7️⃣ distance배열 재선언 & 최소힙에 삽입
  8️⃣ distance배열 `return`

## ✏️20. [15989](https://www.acmicpc.net/problem/15989)

- dp : for문을 두번 따로 돌림!!!

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)
