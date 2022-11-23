'''
< 평범한 배낭 >
https://www.acmicpc.net/problem/12865
문제)
- N개의 물건이 잇다.
- 각 물건은 무게 W와 V를 가진다.
- 준서는 최대 K만큼 무게만 가방에 넣을 수 있다.
- 가방에 들어간 물건 가치의 최댓값???

입력)
- 1     : 물품의 수 N~[1 \ 100], 버틸무게 K~[1 \ 100,000]
- 2[N]  : 각물건의 무게 W, 물건의 가치 V
출력)
- 물건 가치합의 최댓값
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n)]
for i, item in enumerate(items):
    w, v = item
    for j in range(1, k+1):
        if i == 0 and w < j: 
            dp[i][j] = v
        else:
            if w > j: dp[i][j] = dp[i-1][j]        
            else: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
#     print(*dp, sep='\n')
#     print()
# print(*dp, sep='\n')
print(dp[n-1][k])

'''

'''