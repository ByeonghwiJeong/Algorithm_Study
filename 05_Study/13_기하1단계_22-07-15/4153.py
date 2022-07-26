import sys
input = sys.stdin.readline

while True :
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break  
    max_num = max(nums)
    nums.remove(max_num)  
    if nums[0]**2 + nums[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')