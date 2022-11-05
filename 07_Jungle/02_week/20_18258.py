from collections import deque
import sys
input = sys.stdin.readline

def queue(x, i = 0):
    global q
    if x == 'push': q.append(i)
    elif x == 'pop':
        if q: print(q.popleft())
        else: print(-1)
    elif x == 'size': print(len(q))
    elif x == 'empty':
        if q: print(0)
        else: print(1)
    elif x == 'front':
        if q: print(q[0])
        else: print(-1)
    elif x == 'back':
        if q: print(q[-1])
        else: print(-1)


q = deque()
for _ in range(int(input())):
    queue(*input().split())