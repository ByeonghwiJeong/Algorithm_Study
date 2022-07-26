M = int(input())
N = int(input())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n // 2 + 1):    
        if n % i == 0:
            return False
    return True

l = []

for i in range(M, N+1):
    if is_prime(i):
        l.append(i)

if l:
    print(sum(l))
    print(l[0])
else:
    print(-1)