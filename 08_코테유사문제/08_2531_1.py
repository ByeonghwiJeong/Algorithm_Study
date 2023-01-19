'''
< 회전 초밥 >
https://www.acmicpc.net/problem/2531
문제)
- 초밥종류를 번호로 표현, 같은 초밥 있을 수 있음
- 회전초밥집에서 행사 진행
    1. 벨트의 임의의 위치에서 k개의 접시를 연속해서 먹을 경우 할인
    2. 각 고객에는 초밥 번호가 적혀진 쿠폴 발행
        이 번호의 초밥 하나를 무료로 제공
        벨트에 없으면 새로 만들어서 제공
- 손님이 먹을 수 있는 초밥 가짓수의 최댓값?
입력)
- 1     : 접시의 수 n, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
        - n ~ [2 \ 30,000]
        - d ~ [2 \ 3,000]
        - k ~ [2 \ 3,000]
- 2     : 
'''
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
left, right = 0, 0
dict = dict()
ret = 0
# k만큼 먹기
while right < k:
    if a[right] in dict:
        dict[a[right]] += 1
    else: dict[a[right]] = 1
    right += 1
# c는 반드시 추가
if c in dict: dict[c] += 1
else: dict[c] = 1
# 슬라이딩 윈도우
while left < n:
    ret = max(ret, len(dict))
    # a맨 왼쪽 초밥 제거
    dict[a[left]] -= 1
    if dict[a[left]] == 0: del dict[a[left]]
    if a[right % n] in dict: dict[a[right % n]] += 1
    else: dict[a[right % n]] = 1
    left += 1
    right += 1
print(ret)
