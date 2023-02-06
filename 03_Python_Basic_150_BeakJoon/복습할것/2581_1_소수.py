# def is_prime(x):
#     if x == 1:
#         return False
#     for i in range(2, x // 2 + 1):
#         if x % i == 0:
#             return False
#     return True

N = int(input())
M = int(input())
l = []
check = [True] * (M+1)
for i in range(2, M+1):
    if check[i]:
        if N <= i:
            l.append(i)
        for j in range(i*2, M+1, i):
            check[j] = False
if l:
    print(sum(l))
    print(l[0])
else:
    print(-1)
