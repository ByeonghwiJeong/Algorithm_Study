import sys
input = sys.stdin.readline

l = [int(input()) for _ in range(9)]
l.sort()
s = sum(l)
for i in range(8):
    for j in range(i, 9):
        if s - l[i] - l[j] == 100:
            for k in l:
                if k == l[i] or k == l[j]:
                    continue
                print(k)
            exit()