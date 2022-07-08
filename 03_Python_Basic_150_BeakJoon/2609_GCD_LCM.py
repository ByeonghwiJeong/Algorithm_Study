def gcd(x, y):
    z = x % y
    if z == 0:
        return y
    return gcd(y, z)

A, B = map(int, input().split())
g = gcd(A, B)
l = A * B // g
print(g, l, sep='\n')