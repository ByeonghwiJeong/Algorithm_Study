import sys
input = sys.stdin.readline

a = [(1, 2), (3, 4), (5, 6)]
b = [(1, 2)]
c = []
for i in a:
    if i in b:
        continue
    c.append(i)
print(c)