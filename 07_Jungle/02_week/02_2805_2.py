'''
< 이분탐색 while >
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))

def binary_search(st, en, t):
    while st <= en:
        mid = (st + en) // 2
        tot = sum(i - mid for i in a if i > mid)
        if tot == t: return mid
        elif tot < t: en = mid -1
        else: st = mid + 1
    return (st + en) // 2

print(binary_search(0, max(a), m))

'''

'''