'''
문제)
상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램작성
입력)
    - N 숫자카드의 개수
    - 숫자카드에 적혀있는 정수
    - M
    - 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야하는 M개의 정수
'''
import sys
input = sys.stdin.readline

def binary_search(array, st, en, target):
    if st >= en:
        if array[st] == target:
            return 1
        return 0
    mid = (st + en) // 2
    if target == array[mid]:
        return 1
    elif target > array[mid]:
        return binary_search(array, mid+1, en, target)
    else:
        return binary_search(array, st, mid - 1, target)

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums)
M = int(input())
check_nums = list(map(int, input().split()))
for s in check_nums:
    print(binary_search(nums, 0, N - 1, s), end=' ')
