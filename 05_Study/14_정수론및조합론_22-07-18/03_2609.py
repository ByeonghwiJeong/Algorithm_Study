import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10 ** 7

def gcd(x, y):
    z = x % y
    if z == 0:
        return y
    return gcd(y, z)

X, Y = map(int, input().split())
print(gcd(X, Y))
print(X * Y // gcd(X, Y))

