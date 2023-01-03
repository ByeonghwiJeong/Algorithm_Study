n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
l.sort(key = lambda x: (x[1], x[0]))
for i in l:
    print(*i)

