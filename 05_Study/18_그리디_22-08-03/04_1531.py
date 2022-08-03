import sys
input = sys.stdin.readline

S = input().rstrip()

nums = []
cals = []
num = 0

for s in S:
    if s.isdigit():
        num = num*10 + int(s)
    else:
        nums.append(num)
        num = 0
        cals.append(s)
nums.append(num)

# print(nums)
# print(cals)

ans = nums[0]
_minus = False

for i in range(len(cals)):
    if cals[i] == '+':
        if _minus:
            ans -= nums[i+1]
        else:
            ans += nums[i+1]
    elif cals[i] == '-':
        ans -= nums[i+1]
        _minus = True

print(ans)