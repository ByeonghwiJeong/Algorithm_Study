import sys
input = sys.stdin.readline
h, w = map(int, input().split())
l = []

for _ in range(h):
    a = list(input().rstrip())
    for i, v in enumerate(a):
        if v == '.': a[i] = -1
        else: a[i] = 0
    flag = 0
    for i, v in enumerate(a):
        if v == 0:
            flag = 1
        if v == -1 and flag:
            a[i] = flag
            flag += 1
    l.append(a)


for i in l:
    print(*i)