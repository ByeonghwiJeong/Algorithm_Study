'''
< 과자 나눠주기 >
문제)
- 모든 조카에게 같은 길이의 막대과자를 준다.
- 최대한 긴 과자를 나눠주려고 한다.
입력)
- 1     : 조카의수M ~ [1 \ 1,000,000], 
    과자의 수 N ~ [1 \ 1,000,000]
- 2     : 과자 N개의 길이 ~ [1 \ 1,000,000,000]
출력)
- 1     : 조카 1명에게 줄수 있는 막대 과자의 최대 길이
    - 모든 조카에게 같은 길이 막대과자를 나눠줄 수없다면 0출력
'''
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

def count_snack(l):
    cnt = 0
    for s in snacks:
        if s < l: continue
        cnt += s // l
    return cnt

def binary_search(m):
    left = 1
    right = max(snacks)
    while left <= right:
        mid = (left + right) // 2
        if count_snack(mid) >= m:
            left = mid + 1
        else: right = mid - 1
    return left - 1

print(binary_search(m))



'''
 left: 과자 길이의 최솟값 -> 1
 right: 과자 길이의 최댓값
'''