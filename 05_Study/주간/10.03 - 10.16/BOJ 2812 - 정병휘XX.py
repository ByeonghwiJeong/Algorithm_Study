"""
< 크게 만들기 >
https://www.acmicpc.net/problem/2812

N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰수를 구하는 프로그램을 작성하시오.
"""
N, K = map(int, input().split())
nums = list(map(int, list(input().rstrip())))
cnt = 0
while cnt < K:
    tmp = 0
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            tmp = i
            break
    else:
        tmp = len(nums) - 1
    del nums[tmp]
    cnt += 1
print(*nums, sep='')
"""
이전보다 커졌을때 지운다
시간초과발생
"""