import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
  n, s, e, k = map(int, input().split())
  test = list(map(int, input().split()))
  rs = test[s-1:e]
  rs.sort()
  print(f"#{t+1} {rs[k-1]}")

"""
rs 를 정의할때 test[s-1:e].sort()를했는데
나누어서 써야한다.
"""