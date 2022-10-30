import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = int(input())
    ret = 0
    while a >= 5:
        a //= 5
        ret += a
    print(ret)