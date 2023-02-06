import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
chk = [0] * (N+1)
for i in range(2, N+1):
  if chk[i] == 0:
    cnt += 1
    for j in range(i, N+1, i):
      chk[j] += 1

print(cnt)

