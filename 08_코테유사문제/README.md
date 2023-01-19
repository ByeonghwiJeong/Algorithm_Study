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

## ✏️0. [](https://www.acmicpc.net/problem/)

## ✏️0. [](https://www.acmicpc.net/problem/)
