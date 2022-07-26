'''
<계단 오르기>
1. 계단은 한번에 1 or 2
2. 연속된 3개의 계단 xxx
3. 마지막 계단 꼭

10 20 15 25 10 20
10 - [10, 0]
20 - [10+20, 0]
15 - [0, 10+15]
25 - [10+15+25, 10+20+25] 

n-2 : a(n-2,0) a(n-2,1)
n-1 : a(n-1,0) a(n-1,1)
n   : x + a(n-1,1), x + max(a(n-2))
'''
import sys
input = sys.stdin.readline

N = int(input())
_list = []
for _ in range(N):
    _list.append(int(input()))

dp = [[0,0] for _ in range(N)]

if N == 1:
    print(_list[0])
elif N == 2:
    print(sum(_list))
elif N == 3:
    print(_list[0] + _list[-1])
else:
    dp[0][0] = _list[0]
    dp[1][0] = _list[0] + _list[1]
    dp[2][0] = _list[0] + _list[0]
    for i in range(3, N):
        dp[i][0] = _list[i] + dp[i-1][1]
        dp[i][1] = _list[i] + max(dp[i-2])
    print(max(dp[-1]))

    for p in dp:
        print(*p)