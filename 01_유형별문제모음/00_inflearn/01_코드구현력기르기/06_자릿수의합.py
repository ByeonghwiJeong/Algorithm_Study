import sys
input = sys.stdin.readline

def digit_sum(x):
  str_num = str(x)
  sum = 0
  for i in str_num:
    sum += int(i)
  return sum

N = int(input())
nums = list(map(int, input().split()))
sum_list = list(map(digit_sum, nums))
rs_index = sum_list.index(max(sum_list))
print(nums[rs_index])