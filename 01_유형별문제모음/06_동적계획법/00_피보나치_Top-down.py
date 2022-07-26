'''
이코테 피보나치
n1 = 1 n2 = 1 인 피보나치
Top-down
'''
# dp table
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))