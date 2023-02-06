l = []
for _ in range(int(input())):
    l.append(int(input()))
l = sorted(list(set(l)))
print(*l, sep='\n')