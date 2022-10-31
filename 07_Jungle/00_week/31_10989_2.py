import sys
input = sys.stdin.readline

l = [0] * 10001
for _ in range(int(input())):
    l[int(input())] += 1

for i, v in enumerate(l):
    for _ in range(v):
        print(i)

