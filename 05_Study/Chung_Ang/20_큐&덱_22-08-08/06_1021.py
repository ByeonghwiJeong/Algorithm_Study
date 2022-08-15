'''
1 : 큐의 크기 N, 뽑아내려고 하는 수의 개수 M
2 : 뽑아내려고 하는 수의 위치 [1, N]

10 3
2 9 5

1 2 3 4 5 6 7 8 9 10
3 4 5 6 7 8 9 10 1 // 2
index 1 -1 2 -2 3 -3 : -3 > rotate(3) cnt += 3

'''
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_nums = list(map(int, input().split()))
d = deque([i for i in range(1, N +1)])
cnt = 0
for n in _nums:
    i = 0
    pos = True
    while True:
        if d[i] == n:
            break
        if d[-i] == n:
            pos = False
            break
        i += 1
        cnt += 1
    if pos:
        d.rotate(-i)
    else:
        d.rotate(i)
    d.popleft()
print(cnt)