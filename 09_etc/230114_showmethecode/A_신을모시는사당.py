'''
< 신을 모시는 사당 >
문제)
- 돌상 N개가 일렬로 놓여있다.
o o o o o o
- 창영이는 연속한 몇 개의 돌상에 금칠을 한다.
- 깨달음을 얻기위해서는 가능한 많은 금색 돌상이 같은방향
- 방향이 다른 돌상은 깨달음에 치명적이다.

깨달음 = | 왼쪽 금색 돌상 개수 - 오른쪽 금색 돌상 개수 |

입력)
- 1     : 돌상의 개수 N이 주어진다 (1 <= N <= 100,000)
- 2     : 바라보고 있는 방향 (왼쪽 : 1, 오른쪽 : 2)

출력)
- 1     : 최대 깨달음의 양
'''
import sys
input = sys.stdin.readline

N = int(input())
def go(x):
    if x == 2:
        return -1
    return x
a = list(map(go, map(int, input().split())))
dp = [[0] * N for _ in range(2)] # [0]최대 [1]최소 dp   
dp[0][0] = a[0] # 최대 memo 
dp[1][0] = a[0] # 최소 memo

for i in range(1, N):
    # 최대 ~ 연속된 합의 최대값 구하는문제??
    if dp[0][i - 1] + a[i] > a[i]:
        dp[0][i] = dp[0][i - 1] + a[i]
    else: dp[0][i] = a[i]
    # 최소
    if dp[1][i - 1] + a[i] < a[i]:
        dp[1][i] = dp[1][i - 1] + a[i] 
    else: dp[1][i] = a[i]
print(max(max(dp[0]), abs(min(dp[1]))))