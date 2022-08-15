'''
RGB 거리에는 집이 N개 있다.
거리는 선분으로 나타낼 수 있고, 
1번 집부터 N번 집이 순서대로 있다.

집은 Red Green Blue 중하나로 칠해야한다.

아래 규칙을 만족하면서 최소 비용을 구하자
규칙)
1. 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
2. N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
3. i(2<=i<=N+1)번 집의 색은 i-1번, i+1번 집의 색과 같이 않아야 한다.

입력)
    - 첫째 줄에는 집의 수 N 2 ~ 1000
    - 둘째 줄 부터 N개의 출
        - R G B 비용
'''
import sys
input = sys.stdin.readline
N = int(input())
_rgb = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]

dp[0] = _rgb[0][:]

for i in range(1, N):
    dp[i][0] = _rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = _rgb[i][1] + min(dp[i-1][2], dp[i-1][0])
    dp[i][2] = _rgb[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))
# 굳이 _rgb테이블을 생성하지않고 처음 입력받을때 바로 dp에 반영할 수 있다.
'''
n = int(sys.stdin.readline())

cost = [[0, 0, 0]]

for i in range(n):
  temp = [0, 0, 0]
  r, g, b = map(int, sys.stdin.readline().split(" "))
  temp[0] = min(cost[-1][1], cost[-1][2]) + r
  temp[1] = min(cost[-1][0], cost[-1][2]) + g
  temp[2] = min(cost[-1][0], cost[-1][1]) + b
  cost.append(temp)

print(min(cost[-1]))
'''