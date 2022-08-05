'''
1. 2나누기
2. 3나누기
3. 1빼기

10
2: 5
3: x
1: 9

f1: 0
f2: 1
f3: 1 
f4: 1 + (f2 or f3) = 2
f5: 1 + (f4) = 3
f6: 1 + (f3 or f2) = 2
f7: 1 + f6 = 3
f8: 1 + min(f4 or f7) = 3
f9: 1 + min(f8, f3)
f10: 1 + min(f5, f9)

'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 0, 1, 1]
tmp_N = 4
if N > tmp_N:
    tmp_N = N
for i in range(4, tmp_N+1):
    _list = []
    if i % 2 == 0:
        _list.append(dp[i//2])
    if i % 3 == 0:
        _list.append(dp[i//3])
    _list.append(dp[i-1])
    dp.append(1 + min(_list))

print(dp[N])
