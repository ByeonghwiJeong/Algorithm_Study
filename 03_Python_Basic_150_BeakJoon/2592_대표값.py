import sys
input = sys.stdin.readline

nums = []
for _ in range(10):
    nums.append(int(input()))

print(sum(nums) // len(nums))
cnt = {}
for n in nums:
    if n in cnt:
        cnt[n] += 1
    else:
        cnt[n] = 1

for k, v in cnt.items():
    if v == max(cnt.values()):
        print(k)
        break

