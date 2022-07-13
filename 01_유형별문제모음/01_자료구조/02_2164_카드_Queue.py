from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque(range(1, N+1))

while len(dq)>1: # 마지막 한개는 남겨야함
  dq.popleft()
  dq.append(dq.popleft())

print(dq.pop())