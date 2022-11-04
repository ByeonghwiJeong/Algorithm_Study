import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    a = int(input())
    if l:
        while l:
            if l[-1] <= a:
                l.pop()
            else: break
        l.append(a)
    else: l.append(a)
print(len(l))