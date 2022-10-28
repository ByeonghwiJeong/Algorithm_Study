'''
N개의 정수로 이루어진 배열 A
배열을 적절히 바뀌서 최대값을 구하기

범위체크 N ~ [3 \ 8]
시간복잡도 1초
'''
from itertools import permutations
import sys
input = sys.stdin.readline
l = int(input())
_list = list(map(int, input().split()))
result = 0

for s in permutations(_list):
    tmp = 0
    for i in range(len(s)-1):
        tmp += abs(s[i+1] - s[i])
    if tmp > result:
        result = tmp
print(result)
    