'''
지방N은 10,000이하 
선형 탐색시 시간초과 발생 
각 지방N의 예산req은 100,000이하
총예산M은 1,000,000,000
'''
N = int(input())
req = list(map(int, input().split()))
M = int(input())

lo = 0
hi = max(req)
mid = (lo + hi) // 2
ans = 0

def is_possible(mid):
  # tot = 0
  # for r in req:
  #   tot += min(r, mid)
  return sum(min(r, mid) for r in req) <= M

while lo <= hi:
  print(f'lo:{lo}, mid:{mid}, hi:{hi}, ans:{ans}')
  if is_possible(mid):
    lo = mid + 1
    ans = mid
  else:
    hi = mid - 1
  mid = (lo + hi) // 2
  
print(f'마지막 lo:{lo}, mid:{mid}, hi:{hi}, ans:{ans}')
  
print(ans)

