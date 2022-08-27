'''
입력)
- 1 : 수의 개수 N [2 \ 11]
- 2 : N개의 숫자 [1 \ 100]
- 3 : 덧셈0 / 뺄셈1 / 곱셈2 / 나눗셈3
'''
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
_nums = list(map(int, input().split()))
_add, _sub, _mul, _div = map(int, input().split())

_max = -987654321
_min = 987654321

def dfs(i, r):
    global _max, _min, _add, _sub, _mul, _div
    if i == N:
        _max = max(_max, r)
        _min = min(_min, r)
    else:
        if _add > 0:
            _add -= 1
            dfs(i + 1, r + _nums[i])
            _add += 1
        if _sub > 0:
            _sub -= 1
            dfs(i + 1, r - _nums[i])
            _sub += 1
        if _mul > 0:
            _mul -= 1
            dfs(i + 1, r * _nums[i])
            _mul += 1
        if _div > 0:
            _div -= 1
            dfs(i + 1, int(r / _nums[i]))
            # 음수 나누기에서 //로 하면 죄측으로간다
            # 2018/5 = 403.6, 2018//5 = 403, -2018//5 = -404
            _div += 1

dfs(1, _nums[0])
print(_max)
print(_min)