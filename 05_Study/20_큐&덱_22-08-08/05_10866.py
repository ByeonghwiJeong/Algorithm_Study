'''

'''
from collections import deque
import sys
input = sys.stdin.readline

def deq(x, i = 0):
    global _deque
    if x == 'push_front':
        _deque.appendleft(i)
    elif x == 'push_back':
        _deque.append(i)
    elif x == 'size':
        print(len(_deque))
    elif x == 'empty':
        if _deque:
            print(0)
        else:
            print(1)
    elif _deque:
        if x == 'pop_front':
            print(_deque.popleft())
        elif x == 'pop_back':
            print(_deque.pop())
        elif x == 'front':
            print(_deque[0])
        elif x == 'back':
            print(_deque[-1])
    else:
        print(-1)


_deque = deque()
for _ in range(int(input())):
    deq(*input().split())