a = int(input())
b = int(input())
c = int(input())

result = a * b * c
l = [0] * 10
for i in str(result):
    l[int(i)] += 1
print(*l, sep="\n")