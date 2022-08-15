'''
3
headgear 2
eyewear 1
3 2 - 1
4 - 1
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    _dict = dict()
    for _ in range(int(input())):
        a, k = input().split()
        if k in _dict:
            _dict[k] += 1
        else:
            _dict[k] = 1
    ans = 1
    for i in _dict.values():
        ans *= i + 1
    print(ans - 1)