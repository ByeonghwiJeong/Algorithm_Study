'''
- 작은 값부터 측정 가능 한지 확인위해 오름차순정렬
'''
import sys
input = sys.stdin.readline

n = int(input())
W = list(map(int, input().split()))
W.sort()

_max = 0 # 측정 가능 최대 수
for w in W:
    if _max + 1 < w: # _max까지 측정가능 but _max + 1은 건너뛰어서
        break
    _max += w
print(_max + 1)