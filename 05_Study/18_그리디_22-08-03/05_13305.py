'''
어떤 나라에 N개의 도시가 있다. 
'''
import sys
input = sys.stdin.readline

N = int(input())
_distances = list(map(int, input().split()))
_prices = list(map(int, input().split()))

ans = 0
tmp_price = _prices[0]
dis = 0
for i in range(N-1):
    if tmp_price > _prices[i]:
        ans += tmp_price * dis
        dis = 0
        dis += _distances[i]
        tmp_price = _prices[i]
    else:
        dis += _distances[i]
ans += tmp_price * dis
print(ans)
