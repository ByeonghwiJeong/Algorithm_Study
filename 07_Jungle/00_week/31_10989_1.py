import sys
input = sys.stdin.readline

l = dict()
for _ in range(int(input())):
    i = int(input())
    if i in l:
        l[i] += 1
    else:
        l[i] = 1

for k, v in sorted(l.items()):
    for _ in range(v):
        print(k)

