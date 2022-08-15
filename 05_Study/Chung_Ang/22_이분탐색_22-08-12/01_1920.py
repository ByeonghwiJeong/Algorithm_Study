'''
입력)
    -1 : 자연수 N[1, 100000]
    -2 : N개의 정수 [-2^31, 2^31]
    -3 : 자연수 M[1, 100000]
    -4 : M개의 정수 [-2^31, 2^31]
출력)
존재하면 1, 존재하지않으면 0 
'''
import sys
input = sys.stdin.readline

N = int(input())
_N = list(map(int, input().split()))
_N.sort()
M = int(input())
_M = list(map(int, input().split()))

def binary_search(st, en, target):
    if st > en:
        print(0)
        return
    mid = (st + en) // 2
    if _N[mid] == target:
        print(1)
        return
    elif _N[mid] < target:
        binary_search(mid+1, en, target)
    else:
        binary_search(st, mid-1, target)

for i in _M:
    binary_search(0, N - 1, i)
    