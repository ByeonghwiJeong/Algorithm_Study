'''
https://www.acmicpc.net/problem/3687
제목 : 성냥개비

문제)
- 성냥개비로 숫자표현
- 가장 작은 수 & 가장 큰 수 출력

1 : 2개
2 : 5개
3 : 5개
4 : 4개
5 : 5개
6 : 6개
7 : 3개
8 : 7개
9 : 6개
0 : 6개

입력)
- 1 : 테스트 케이스의 개수 ~ [1, 100]
- 2 : 테스트 케이스의 숫자 ~ [2, 100]
'''
'''
# 1자리 숫자로 사용되는 최대 성냥개비 수 : 7개
# 성냥개시 수 2 ~ 7까지 : 1, 7, 4, 2, 6, 8

# check_list index 6인경우 6개의 성냥개비로 0을 표현할 수 있음
# (첫번째 자리 아닌경우 6 -> 0으로 변경)
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [''] * 101
check_list = ['', '', '1', '7', '4', '2', '6', '8']


for i in range(2, 8):
    dp[i] = check_list[i]

for i in range(8, 101):
    for j in range(2, i - 1):
        candidate = dp[j] + dp[i - j]
        dp[i] = candidate if dp[i] == '' else min(dp[i], candidate, key=int)
        if j == 6:  # '6'개의 성냥개비로는 '0'을 사용할 수 있다.
            candidate_with_zero = dp[i - j] + '0'
            dp[i] = candidate_with_zero if dp[i] == '' else min(dp[i], candidate_with_zero, key=int)


def max_process(n):
    if n % 2:
        return '7' + '1' * ((n-3)//2)
    else:
        return '1' * (n//2)
    

def min_process(n):
    return dp[n]

for _ in range(int(input())):
    n = int(input())
    print(min_process(n), max_process(n))
        