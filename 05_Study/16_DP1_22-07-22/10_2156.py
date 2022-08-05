'''
<포도주 시식>
1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주를 모두 마셔야하고,
    마신 후에는 원래 위치에 다시 놓아야한다.
2. 연속으로 놓여 있는 3잔을 마실수없다.
    - 연속으로 2번 연속 : 1칸씩 이동
1부터 n까지 번호순서대로 있다.
6 10 13 9 8 1
V V     V V 
6
6+10 10
13+10 13+6

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
    print(max(_list[0] + _list[-1], _list[1] + _list[2], _list[0] + _list[1]))
else:
    dp[0] = [_list[0], _list[0]]
    dp[1] = [_list[0] + _list[1], _list[1]]
    dp[2] = [_list[2] + _list[1], _list[0] + _list[2]]
    for i in range(3, N):
        dp[i][0] = _list[i] + dp[i-1][1]
        dp[i][1] = _list[i] + max(dp[i-2])
    print(max(dp[-1]+dp[-2]))