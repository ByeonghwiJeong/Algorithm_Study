import sys
input = sys.stdin.readline

N = int(input())
awards = []

for i in range(N):
  tmp = input().split()
  tmp.sort()
  a, b, c = map(int, tmp)
  if a == b and b == c:
    money = 10000 + a * 1000
  elif a == b or b == c:
    money = 1000 + b * 100
  else:
    money = c * 100
  awards.append(money)

print(max(awards))
