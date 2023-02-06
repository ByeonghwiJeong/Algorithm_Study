import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
cnt = 1
rs = 0
for num in nums:
  if num == 0:
    cnt = 1
  else:
    rs += cnt
    cnt += 1
print(rs)