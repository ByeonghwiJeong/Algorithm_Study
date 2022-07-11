N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))
l.sort()
print(*l, sep='\n')

