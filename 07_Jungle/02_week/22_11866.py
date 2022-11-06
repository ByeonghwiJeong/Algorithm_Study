'''
< 요세푸스 문제 >
https://www.acmicpc.net/problem/11866
문제)
- 1 ~ N번까지 N명의 사람이 원을 이루면서 앉아있다.
- K번째 사람을 제거한다.
- 이과정에서 N명의 사람이 모두 제거될 때까지 계속 반복
- 원에서 사람들이 제거되는 순서를 (N, K) 요세푸스 순열
- 예) (7, 3)
    - 3, 6, 2, 7, 5, 1, 4

입력)
- 
출력)
- 
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque(range(1, n+1))
ans = []
while q:
    q.rotate(-k)
    ans.append(q.pop())
    
print('<', end='')
print(*ans, sep=', ', end='>')


