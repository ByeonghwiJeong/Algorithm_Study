'''

'''

import sys
input = sys.stdin.readline

def in_circle(x, y, r, a, b):
    if (a - x)**2 + (b - y)**2 <= r**2:
        return 1
    return 0

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())
        if in_circle(cx, cy, r, x1, y1) != in_circle(cx, cy, r, x2, y2):
            cnt += 1
    print(cnt)

