N = int(input())
m = 2
while N != 1:
    if N % m == 0:
        print(m)
        N //= m
    else:
        m += 1