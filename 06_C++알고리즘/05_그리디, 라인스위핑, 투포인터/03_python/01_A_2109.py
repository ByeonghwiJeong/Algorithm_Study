"""
[순회강연]
https://www.acmicpc.net/problem/2109
문제)
n~[0, 10,000]개의 대학에서 순회강연을 요청
각 대학에서는 d~[1, 10,000]일 안에 와서 강연을 해주면 p~[1, 10,000]만큼의 pay를 지급
가장 많은 cache를 벌 수 있는 금액을 출력
팁)
최대 : 최소를 작게만들거나 최대를 크게 만듬
"""
import sys
import heapq
input = sys.stdin.readline

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort(key=lambda x: (x[1], x[0]))
answer = 0
money = []
for p, d in lectures:
    heapq.heappush(money, p)
    if len(money) > d:
        heapq.heappop(money)

print(sum(money))