import sys
input = sys.stdin.readline

n, s = map(int, input().split())
coins = [ int(input()) for _ in range(n) ]
coins.reverse()
ans = 0 
for coin in coins:
  ans += s // coin
  s %= coin
print(ans)