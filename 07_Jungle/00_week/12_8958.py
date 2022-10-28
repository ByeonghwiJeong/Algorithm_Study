import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    a = 0
    sum = 0
    for i in s:
        if i == 'O':
            a += 1
            sum += a
        else:
            a = 0
    print(sum)