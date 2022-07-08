l = []

for i in range(1, 9):
    a = int(input())
    l.append((a, i))

ans = sorted(l, reverse=True)[:5]
ans = sorted(ans, key=lambda x:x[1])

sum = 0
num = []
for i in ans:
    sum += i[0]
    num.append(str(i[1]))
print(sum)
print(' '.join(sorted(num)))