l = []
for _ in range(int(input())):
    l.append(tuple(map(int, input().split())))

l.sort(key=lambda x:(x[0], x[1]))
for i in l:
    print(*i)