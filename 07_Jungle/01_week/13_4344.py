import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, *a = map(int, input().split())
    ave = sum(a) / x
    b = 0
    for i in a:
        if i > ave:
            b += 1
    # print(round(b / x * 100, 3), end="")
    # print("%")
    print(f'{b / x * 100:.3f}%')