'''
< 사냥꾼 - >
https://www.acmicpc.net/problem/8983
문제)
- N마리의 동물들이 각각 특정한 위치에 살고 있다.
- 사냥꾼은 일직선 상에 위치한 M개의 사대에서만 사격가능
- 일직선을 x축
- 동물이 사는 위치 (a1, b1), (a2, b2), (a3, b3) ... (an, bn)
- 총의 사정거리 L : 
- 동물~사람거리: |xi-an| + bn
입력)
- 1     : 사대수 m ~ [1 \ 100,000], \
             동물의 수 n ~ [1 \ 100,000], \
                사정거리 L ~ [1 \ 1,000,000,000]
- 2     : 사대의 위치 M개의 x좌표
- 3[n]  : (x, y) 
출력)
- 
'''
import sys
from bisect import bisect_left
input = sys.stdin.readline
m, n, l = map(int, input().split())
x = sorted(list(map(int, input().split())))
a = [tuple(map(int, input().split())) for _ in range(n)]

def near_x(t):
    idx = bisect_left(x, t)
    if idx == 0: return x[0]
    if idx == m: return x[-1]
    l = x[idx - 1]
    r = x[idx]
    if t - l < r - t:
        return l
    return r
    
ret = 0
for ax, ay in a:
    xv = near_x(ax)
    if abs(xv - ax) + ay <= l:
        ret += 1
print(ret)
'''


'''