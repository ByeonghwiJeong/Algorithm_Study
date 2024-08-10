'''
https://www.acmicpc.net/problem/12865
문제 : 평범한 배낭

- 기본적인 배낭 문제
- 여행에 필요한 N개의 물건
- 각 물건은 무게 W와 가치 V
- 배낭에 넣을 수 있는 무게 K
- 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 구하라.

입력)
- 1 : N ~ [1, 100], K ~ [1, 100000]
- 2 ~ N+1 : W ~ [1, 100000], V ~ [0, 1000]
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]
# dp[i][w]는 i번째 물건까지 고려했을 때, 무게 w에서의 최대 가치를 저장

for i in range(1, N + 1): # i번째 물건
    for j in range(1, K + 1): # 고려중 무게
        w, v = items[i - 1]
        # i번째 무게, 가치
        if j < w: # 물건을 넣을 수 없는 경우 
            dp[i][j] = dp[i - 1][j] # 이전 물건까지 고려했을 때의 최대 가치
        else: # 물건을 넣을 수 있는 경우
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            # 이전 물건까지 고려했을 때의 최대 가치와 
            # i번째 물건을 넣었을 때의 최대 가치 중 큰 값을 선택

print(dp[N][K])
        