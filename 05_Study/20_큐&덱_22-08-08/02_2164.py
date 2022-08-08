'''
N장의 카드 1 ~ N
1번 카드가 제일 위 
N번 카드가 제일 아래

1. 제일 위 카드 버린다 
2. 제일 위 카드 밑으로 옮긴다.

N = 4 
1234
234
342
42
24
4
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
_nums = [i for i in range(1, N + 1)]
x = deque(_nums)

while len(x) > 1:
    x.popleft()
    x.rotate(-1)

print(x[0])