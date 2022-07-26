'''
N : 가지고 있는 카드 개수
(1 <= N <= 500,000)
M : 숫자 카드에 적혀있는 정수
(-10,000,000 <= M <= 10,000,000)
출력)
    상근이가 몇 개 가지고 있는지
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
chk = list(map(int, input().split()))

nums_dict = dict()
for i in nums: 
    if i in nums_dict:
        nums_dict[i] += 1
    else:
        nums_dict[i] = 1
# print(nums_dict)
for i in chk:
    if i in nums_dict:
        print(nums_dict[i], end=' ')
    else:
        print(0, end=' ')