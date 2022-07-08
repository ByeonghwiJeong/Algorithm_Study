import sys
input = sys.stdin.readline

N,K = map(int, input().split())
nums = list(map(int, input().split()))
each = 0
# K개를 더해주기
for i in range(K):
    each += nums[i]
maxv = each

# 다음인덱스 더해주고, 이전인덱스 빼주기
for i in range(K, N):
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv, each)

print(maxv)