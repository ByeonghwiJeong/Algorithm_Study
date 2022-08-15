'''
자르는 길이가 
'''
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
_list = [int(input()) for _ in range(K)]

# def count(n):
#     cnt = 0
#     for i in _list:
#         cnt += i // n
#     return cnt

# def binary_search(st, en, target):
#     if st > en:
#         return en

#     mid = (st + en) // 2
#     if count(mid) >= N:
#         return binary_search(mid + 1, en, target)
#     else:
#         return binary_search(st, mid - 1, target)

# print(binary_search(1, max(_list), N))

st = 1
en = max(_list)

while st <= en:
    mid = (st + en) // 2 # 자르는 길이
    cnt = 0 # 잘린 갯수 구하기
    for i in range(K):
        cnt += _list[i] // mid
    if cnt >= N: 
    # 갯수가 목표보다 크거나 같은경우
    # 
        st = mid + 1
    else:
    # 갯수가 목표보다 작은 같은경우 
    # 
        en = mid - 1
print(en)
    

