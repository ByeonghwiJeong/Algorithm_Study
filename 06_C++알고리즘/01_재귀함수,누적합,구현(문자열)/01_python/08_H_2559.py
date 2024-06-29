import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))
tmp_sum = 0
psum = [0]
ret = -1000000
for i in temp:
    tmp_sum += i
    psum.append(tmp_sum)
for i in range(K, N + 1):
    ret = max(ret, psum[i] - psum[i - K])
print(ret)