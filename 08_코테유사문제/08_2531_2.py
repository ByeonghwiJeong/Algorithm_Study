'''
< defaultdict >
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
left, right = 0, 0
dict = defaultdict(int)
ret = 0
# k만큼 먹기
while right < k:
    dict[a[right]] += 1
    right += 1
# c는 반드시 추가
dict[c] += 1
# 슬라이딩 윈도우
while left < n:
    ret = max(ret, len(dict))
    # a맨 왼쪽 초밥 제거
    dict[a[left]] -= 1
    if dict[a[left]] == 0: del dict[a[left]]
    dict[a[right % n]] += 1
    left += 1
    right += 1
print(ret)
