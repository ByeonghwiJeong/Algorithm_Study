from collections import deque

d = deque('ghi')
d.append('j')
d.appendleft('f')
print(d)
d.pop() # 'j'
d.popleft() # 'f'
list(d)
print(d[0])
print(len(d))