'''
< 1,2,3 더하기 4 >
https://www.acmicpc.net/problem/15989
문제)
- 정수 4를 1 2 3의 합으로 나타내는 방법은 총 4가지이다.
- 순서 다른것은 같은것으로 친다.
- 1+1+1+1
- 2+1+1
- 2+2
- 1+3
입력)
- 1     : 테스트케이스T
- 2[T]  : 정수n
출력)
- 1[T]  : 갯수
'''
import sys
input = sys.stdin.readline

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i-2]
for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(int(input())):
    print(dp[int(input())])