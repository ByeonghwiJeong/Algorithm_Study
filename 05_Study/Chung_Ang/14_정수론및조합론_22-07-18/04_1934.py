import sys
input = sys.stdin.readline

def gcd(x, y):
    z = x % y
    if z == 0:
        return y
    return gcd(y, z)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))