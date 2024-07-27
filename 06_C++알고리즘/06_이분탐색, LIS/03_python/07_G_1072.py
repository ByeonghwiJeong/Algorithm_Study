'''
https://www.acmicpc.net/problem/1072
문제 : 게임

- 게임 횟수 : X
- 이긴 게임 : Y (Z%)
- Z는 형택이의 승률 (소수점 이하 버림)
- X, Y가 주어졌을 때 최소 몇 번 더 이겨야 승률이 변하는지 구하기 (계속 이긴다)
- 승률 변하지 않는다면 -1 출력

입력)
- X, Y ~ [1 \ 1,000,000,000] ~ 0 <= Y <= X
출력)
- 승률이 변하는 최소 횟수
'''
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = Y * 100 // X  # 형택이의 승률
l = 0
h = 10**9
sol = -1

if Z >= 99:
    print(-1)
    exit()

while l <= h:
    mid = (l + h) // 2
    if Z < (Y + mid) * 100 // (X + mid): # 승률이 변한다면
        sol = mid
        h = mid - 1
    else:
        l = mid + 1

print(sol)