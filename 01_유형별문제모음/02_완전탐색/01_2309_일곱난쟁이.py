import sys
input = sys.stdin.readline
from itertools import combinations

# member = []
# for _ in range(9):
#   member.append(int(input()))

# max = []
# for i in combinations(member, 7):
#   if sum(i) == 100:
#     for h in sorted(i):
#       print(h)
#     break
    
heights = [int(input()) for _ in range(9)]
tot = sum(heights)
heights.sort()
breaker = True
for i in range(9):
  for j in range(i+1,9):
    if tot - heights[i] - heights[j] == 100:
      del heights[i]
      del heights[j]
      breaker = False
      break
  if breaker == False:
    break
for i in heights:
  print(i)
  


