'''
[소가 길을 건너간 이유 3]
https://www.acmicpc.net/problem/14469
문제)
N마리의 소가 길을 건너려고 함
N줄에 도착시간, 검문시간 주어짐
'''
import sys
input = sys.stdin.readline

n = int(input())
cows = [tuple(map(int, input().split())) for _ in range(n)]
cows.sort()
time = 0
for cow in cows:
    if time < cow[0]:
        time = cow[0] + cow[1]
    else:
        time += cow[1]

print(time)