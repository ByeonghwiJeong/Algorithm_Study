import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    a = int(a)
    for i in b:
        for _ in range(a):
            print(i, end='')
    print()