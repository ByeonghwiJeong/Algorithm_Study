'''
양의 정수 x의 각자리가 등차수열을 이룬다.
그 수를 한수라고 한다.
n이 주어졌을 때 1보다 크거나 같고,
n보다 작거나 같은 한수의 개수를 출력


'''
import sys
input = sys.stdin.readline

dp = [0] * 1001
dp[1] = 1
for i in range(2, 100):
    dp[i] = dp[i-1] + 1
for i in range(100, 1001):
    i = str(i)
    if int(i[2]) - int(i[1]) == int(i[1]) - int(i[0]):
        i = int(i)
        dp[i] = dp[i-1] + 1
    else:
        i = int(i)
        dp[i] = dp[i-1]
print(dp[int(input())])