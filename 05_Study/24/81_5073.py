"""
https://www.acmicpc.net/problem/5073
"""

import sys
input = sys.stdin.readline

while True:
    a, b, c = sorted(map(int, input().split()))

    if a == 0 and b == 0 and c == 0:
        break
    elif a == b == c:
        print("Equilateral")
    elif a + b <= c:
        print("Invalid")
    elif a == b or b == c:
        print("Isosceles")
    else:
        print("Scalene")



