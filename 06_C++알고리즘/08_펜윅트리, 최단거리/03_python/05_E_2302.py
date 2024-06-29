"""
https://www.acmicpc.net/problem/2302
백준 2302. 극장 좌석, S1
- 왼쪽부터 1번, 2번, ... , N번까지 번호가 붙은 좌석
- 자기 번호에 앉아야함
    - 자기 바로 옆좌석에는 앉을 수 있음 
    - 5번 > 4번, 6번 OK
- VIP고객들은 자기 좌석에만 앉아야함
- 사람들이 좌석에 앉는 경우의 수
입력)
- 좌석의 수 N ~ [1, 40]
- 고정석의 수 M ~ [0, N]
- M줄 ~ VIP고객의 좌석 번호
"""
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
cnt = [0] * 41
for _ in range(M):
    cnt[int(input()) - 1] = 1
dp = [-1] * 41

def go(pos):
    if pos == N - 1: return 1 
    if cnt[pos]: return go(pos + 1)
    if dp[pos] != -1: return dp[pos]
    dp[pos] = 0
    if not cnt[pos + 1]: dp[pos] += go(pos + 1) + go(pos + 2)
    else: dp[pos] += go(pos + 1)
    return dp[pos]

print(go(0))

