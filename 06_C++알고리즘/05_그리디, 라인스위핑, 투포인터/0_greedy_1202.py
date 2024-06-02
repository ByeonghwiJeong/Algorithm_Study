'''
[Title] 보석 도둑
https://www.acmicpc.net/problem/1202
gems정렬 : 오름차순 (무게, 가격)
'''
import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort()
bags.sort()
answer = 0
price_temp = []
for bag in bags: # 각 가방의 최대 무게
    while gems and bag >= gems[0][0]: # 제일 가벼운 보석부터
        heapq.heappush(price_temp, -gems[0][1]) # 최대힙 (heapq는 최소힙, -로 최대힙)
        # gems.pop(0) # TODO : 속도
        heapq.heappop(gems)

    if price_temp:
        answer -= heapq.heappop(price_temp)
print(answer)