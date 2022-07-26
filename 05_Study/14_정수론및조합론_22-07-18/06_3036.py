import sys
input = sys.stdin.readline

def gcd(x, y):
    z = x % y
    if z == 0:
        return y
    return gcd(y, z)

N = int(input())
rings = list(map(int, input().split()))
for i in range(1, N):
    a = rings[0]
    b = rings[i]
    print(a//gcd(a, b), b//gcd(a, b), sep='/')