'''
< 2가지 풀이 >
이분탐색은 어떤식으로 사용?
'''
from bisect import bisect_left, bisect_right

N = int(input())
_N = list(map(int, input().split()))
_N.sort()
M = int(input())
_M = list(map(int, input().split()))


# _dict = dict()
# for i in _N:
#     if i in _dict:
#         _dict[i] += 1
#     else:
#         _dict[i] = 1

# for i in _M:
#     if i in _dict:
#         print(_dict[i])
#     else:
#         print(0)

for i in _M:
    print(bisect_right(_N, i) - bisect_left(_N, i))