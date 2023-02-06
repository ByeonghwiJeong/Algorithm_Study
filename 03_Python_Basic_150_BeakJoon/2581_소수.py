def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

N = int(input())
M = int(input())
l = []
for i in range(N, M+1):
    if is_prime(i):
        l.append(i)
if l:
    print(sum(l))
    print(l[0])
else:
    print(-1)
