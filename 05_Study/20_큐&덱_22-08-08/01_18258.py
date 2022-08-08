'''

'''
from collections import deque
import sys
input = sys.stdin.readline

def queue(x, i = 0):
    global _queue
    if x == 'push':
        _queue.append(i)
    elif x == 'pop':
        if _queue:
            print(_queue.popleft())
        else:
            print(-1)
    elif x == 'size':
        print(len(_queue))
    elif x == 'empty':
        if _queue:
            print(0)
        else:
            print(1)
    elif x == 'front':
        if _queue:
            print(_queue[0])
        else:
            print(-1)
    elif x == 'back':
        if _queue:
            print(_queue[-1])
        else:
            print(-1)

_queue = deque()
for _ in range(int(input())):
    queue(*input().split())