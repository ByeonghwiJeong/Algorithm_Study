'''
[컵라면]
https://www.acmicpc.net/problem/1781
문제)
N개의 문제, 각각의 문제는 데드라인과 컵라면 수가 주어짐
최대 컵라면 수 출력
'''
import sys, heapq
input = sys.stdin.readline
n = int(input())
problems = [tuple(map(int, input().split())) for _ in range(n)]
problems.sort(key=lambda x: (x[0], -x[1])) # 데드라인 오름차순, 컵라면 내림차순
hq = []

for d, r in problems:
    heapq.heappush(hq, r)
    if len(hq) > d:
        heapq.heappop(hq)

print(sum(hq))