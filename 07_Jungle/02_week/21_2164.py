'''
< 카드 >
https://www.acmicpc.net/problem/2164
문제)
- N장의 카드가 있다. 
- 1번 ~ N번까지 번호
    - 1번 : 제일 위
    - N번 : 제일 아래
- 카드가 한 장 남을 때까지 반복하게 된다.
    - 제일 위에 있는 카드를 바닥에 버린다.
    - 그 다음, 제일 위에 있는 카드를 제일 아래로
    - 예) N = 4
    - 1 2 3 4 >> 2 3 4 >> 3 4 2
    - 3 4 2 >> 4 2 >> 2 4
    - 2 4 >> 4 >> 4
입력)
- N ~ [1 \ 500,000]
출력)
- 남게 되는 카드의 번호를 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(range(1, n + 1))
while n > 1:
    q.popleft()
    q.append(q.popleft())
    # q.rotate(-1)
    n -= 1
print(*q)