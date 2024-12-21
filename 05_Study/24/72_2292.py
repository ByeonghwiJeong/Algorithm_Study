"""
https://www.acmicpc.net/problem/2292
제목: 벌집

문제)
1
1 + 6*1 = 7 (2)
1 + 6*1 + 6*2 = 19 (3)
1 + 6*1 + 6*2 + 6*3 = 37 (4)

입력)
13
출력)
3
"""
import sys
input = sys.stdin.readline

N = int(input())

def cal(N):
    return 3*N*(N+1) + 1

if N == 1:
    print(1)
else:
    i = 1
    while True:
        if cal(i-1) < N <= cal(i):
            print(i+1)
            break
        i += 1


