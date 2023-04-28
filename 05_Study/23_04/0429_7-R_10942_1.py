"""
< 팰린드롬? >
https://www.acmicpc.net/problem/10942
문제)
- 명우, 홍준 팰린드롬 놀이
- 홍준이는 자연수 N개를 칠판에 적음
- 명우에게 질문을 총 M번 한ㄷ.
- 각 질문에는 두 정수 S와 E (1 <= S <= E <= N)
    - S번째 수에서 E번째 까지 팰린드롬인지?
- 
"""
import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]

def check(l, r): # l, r 실제 인덱스 위치 기준 
    global dp
    while l <= r and l >= 0 and r < N:
        if not a[l] == a[r]: break
        dp[l][r] = 1
        l -= 1
        r += 1

for i in range(N):
    check(i, i)
    check(i, i + 1)
# print(*dp, sep='\n')

for _ in range(int(input())):
    r, c = map(lambda x: int(x) - 1, input().split())
    print(dp[r][c])

    