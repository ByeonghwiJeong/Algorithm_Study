'''
< 용액 문제 - 이진탐색>
https://www.acmicpc.net/problem/2110
문제)
- 산성용액 & 알칼리성용액
- 산성 ~ [1 \ 1,000,000,000]
- 알칼리 ~ [-1,000,000,000 \ -1]
- 같은 양의 두 용액 혼합시 특성값 : 각각의 특성합

- 같은 양의 두 용액을 혼합해서 0에 가까운 용액을 만들려고 한다

입력)
- 1     : 용액수 N ~ [2 \ 100,000]
- 2[N]  : 용액의 특성값들 

출력)
- 가장 인접한 두 공유기 사이의 최대 거리
'''
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
min = float('inf')
idx1, idx2 = 0, 0

if n == 2:
    print(a[0], a[1])
    exit(0)

def binary_search(st, en):
    global idx1, idx2, min
    mid = (st + en) // 2
    if st > en: return
    tot = a[i] + a[mid]
    if abs(tot) < min:
        idx1, idx2, min = i, mid, abs(tot)
    if tot < 0: binary_search(mid+1, en)
    else: binary_search(st, mid - 1)

for i in range(n - 1):
    start = i + 1
    end = n - 1
    binary_search(start, end)

print(a[idx1], a[idx2])
'''
한용액을 기준으로 a[i] : 고정
a[i+1] ~ a[n - 1] : 이진탐색
for문 1 ~ n-2 : 
'''