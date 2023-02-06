# 반복문 방식
# 메모이제이션 O
# bottom-up
MOD = 10007
cache = [[0] * 1001 for _ in range(1001)]
N, K = map(int, input().split())

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j] + cache[i-1][j-1]
        cache[i][j] %= MOD

# for i in range(7):
#     print(cache[i][:10])

# print()
print(cache[N][K])