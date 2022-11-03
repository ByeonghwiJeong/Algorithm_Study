import sys
input = sys.stdin.readline

nums = []
for _ in range(9):
    nums.append(int(input()))
result = 0
index = 0
for i, v in enumerate(nums):
    if result < v:
        result = v
        index = i
print(result)
print(index + 1)