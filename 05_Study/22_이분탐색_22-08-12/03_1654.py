'''

'''
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
_list = [int(input()) for _ in range(K)]

def count(n):
    cnt = 0
    for i in _list:
        cnt += i // n
    return cnt

def binary_search(st, en, target):
    if st > en:
        return en

    mid = (st + en) // 2
    if count(mid) == N:
        return mid
    elif count(mid) > N:
        return binary_search(mid + 1, en, target)
    else:
        return binary_search(st, mid - 1, target)

print(binary_search(1, max(_list), N))

# -------- 다시 생각해보자
# low = 1
# high = max(_list)
# result = 0
# while low < high:
#     mid = (low + high) // 2
#     if count(mid) >= N:
#         low = mid + 1
#         result = mid
#     else:
#         high = mid - 1
# print(low)