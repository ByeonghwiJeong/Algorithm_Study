'''
< 공유기 설치 >
https://www.acmicpc.net/problem/2805
문제)
- 집N개가 수직선 위에 있다.
- 각각 좌표 x1, x2, x3, ... ,xn
- 한집에는 공유기를 하나만 설치할 수 있다.
- 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성

입력)
- 1     : 집의 개수 N ~ [2 \ 200,000] 공유기의 개수 C ~ [2 \ N]
- 2[N]  : 집의 좌표

출력)
- 가장 인접한 두 공유기 사이의 최대 거리
'''
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])

def count_router(st, en):
    cnt = 1
    now = a[0]
    for i in a:
        if now + (st + en) // 2 <= i: # 공유기설치
            cnt += 1
            now = i
    return cnt

def binary_search(st, en):
    ret = 0
    while st <= en:
        mid = (st + en) // 2
        b = count_router(st, en)
        if b >= c: 
            st = mid + 1 # 거리늘리기
            ret = mid
        elif b < c: en = mid - 1 # 거리줄이기
    return ret

print(binary_search(1, a[-1] - a[0])) # 공유기거리 최소, 최대 

'''

'''