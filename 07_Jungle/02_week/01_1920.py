'''
< 수찾기 >
https://www.acmicpc.net/problem/1920
문제)
- A1, A2, ..., AN 이 주어졌을 때 이안에 x라는 정수가 존재하는지?
입력)
-   1 : 자연수N~[1 \ 100,000]
-   2 : A1, A2, ..., AN
-   3 : M ~ [1 \ 100,000]
-   4 : M개의 수
    - 이 수들이 a안에 존재하는지?
'''
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

def binary_search(st, en, t):
    if st > en: return 0
    mid = (st + en) // 2
    if a[mid] == t: return 1
    elif a[mid] < t: return binary_search(mid+1, en, t)
    else: return binary_search(st, mid-1, t)

for i in b:
    print(binary_search(0, n-1, i))
    