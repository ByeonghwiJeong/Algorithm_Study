'''
r1 + r2 < d 이면 두 원은 서로의 외부에 위치한다.
r1 + r2 = d 이면 두 원은 외접한다.
|r1 - r2| < d < r1 + r2 이면 두 원은 서로 다른 두 점에서 만난다.
|r1 - r2| = d 이면 한 원이 다른 원에 내접한다.
|r1 - r2| > d, r1 ≠ r2 이면 한 원이 다른 원의 내부에 있다.
'''

from math import sqrt
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if r == 0:
        if r1 == r2: # 동심 / 반지름 같음
            print(-1)
        else:
            print(0)
    else:
        if abs(r1 - r2) == r or r1 + r2 == r: # 내접 외접
            print(1)
        elif abs(r1 - r2) < r and r < r1 + r2:
            print(2)
        else:
            print(0)