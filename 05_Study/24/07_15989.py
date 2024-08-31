'''
https://www.acmicpc.net/problem/15989
제목 : 1, 2, 3 더하기 4

문제)
- 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다.
- 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
- 순서만 다른 것은 같은 것으로 친다.

ex) 1+1+1+1, 1+1+2 (1+1+2, 1+2+1), 1+3(3+1), 2+2, 4

입력)
- 1		: 테스트 케이스 T (1 <= T <= 10,000)
- 2	 (T): N (0 <= N <= 10,000)
'''

import sys
input = sys.stdin.readline

dp = [0]*10001

dp[0] = 1 
dp[1] = 1
# d[i] : i를 1, 2, 3의 합으로 나타내는 방법의 수

for i in range(1, 10001): 
    dp[i] += dp[i-1]

for i in range(2, 10001): 
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]


for _ in range(int(input())):
    print(dp[int(input())])
