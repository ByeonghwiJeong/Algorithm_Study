'''
https://www.acmicpc.net/problem/11047
'''
N, K = map(int, input().split())
_coins = []
for _ in range(N):
    _coins.append(int(input()))

cnt = 0
for coin in reversed(_coins):
    cnt += K // coin 
    K %= coin

print(cnt)
