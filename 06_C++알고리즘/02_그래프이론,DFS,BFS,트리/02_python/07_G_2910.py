import sys
input = sys.stdin.readline

n, c = map(int, input().split())
a = list(map(int, input().split())) # 순서
b = dict()
c = set()
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
result = ""
for i in a:
    if i not in c:
        c.add(i)
        for _ in range(b[i]):
            result += f'{i} '
print(result)
