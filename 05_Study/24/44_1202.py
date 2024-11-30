'''
https://www.acmicpc.net/problem/1202
제목: 보석 도둑

문제
- 보석을 훔치려고 한다.
- 보석은 N개가 있고, 각각의 보석은 무게(Mi)와 가격(Vi)이 있다.
- 가방은 K개가 있고, 각각의 가방에 담을 수 있는 최대 무게(Ci)가 있다.
- 가방에는 최대 한 개의 보석만 넣을 수 있다.

입력
- 1 : N, K ~ [1 \ 300,000]
- 2 ~ N+1 (N) : Mi, Vi ~ [1 \ 1,000,000]
- N+2 ~ N+K+1 (K): Ci ~ [1 \ 100,000,000]

출력
- 훔칠 수 있는 보석의 최대 가격의 합을 출력하라.
'''
import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jewels.sort(key=lambda x: x[0]) # 무게 오름차순 정렬 
bags.sort() # 무게 오름차순 정렬

ans = 0
heap = []
jewel_idx = 0 # 보석 인덱스

for bag in bags: # 각 가방에 대해
    while jewel_idx < N and jewels[jewel_idx][0] <= bag: 
        # 보석의 무게가 가방의 최대 허용 무게보다 작거나 같다면
        heapq.heappush(heap, -jewels[jewel_idx][1])
        # 최소힙만 지원하므로 음수로 최대힙 사용 -> 나중에 다시 음수로 변환
        jewel_idx += 1
    
    # 가방에 넣을 수 있는 보석이 있다면 가장 비싼 보석을 넣음
    if heap:
        ans -= heapq.heappop(heap)

print(ans)