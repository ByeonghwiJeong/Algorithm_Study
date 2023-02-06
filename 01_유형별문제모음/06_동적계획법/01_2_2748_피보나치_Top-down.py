# 캐시처리 Memoization
cache = [-1] * 91
cache[0] = 0
cache[1] = 1
# cnt = 0 

def f(n):
    # global cnt
    # cnt += 1
    if cache[n] == -1:
        cache[n] = f(n-1) + f(n-2)
    return cache[n]

print(f(int(input())))
# print(f'cnt: {cnt}')