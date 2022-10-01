"""
< 과제 >
https://www.acmicpc.net/problem/13904
- 하루에 한 과제 가능
- 과제마다 마감일
- 과제마다 끝냈을때 얻을 수 있는 점수가 있음
- 마감일이 지난 과제는 점수를 받을 수 없다.
- 웅찬이의 최대 점수?
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = []
dp = [0] * 1001
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
arr.sort() # 마감 날짜순 정렬
# print(*arr, sep="\n")
for d, w in arr:
    if dp[d-1] == 0:
        dp[d-1] = w
    else:
        min_value = 987654321
        for i in range(d):
            if min_value > dp[i]:
                min_value = dp[i]
                index = i
        dp[index] = w
print(dp[:10])
print(sum(dp))
'''
- DP배열을 만든다.
- arr를 loop돌면서 dp에 넣고 dp에 있는경우 min값 체크를 한다
'''