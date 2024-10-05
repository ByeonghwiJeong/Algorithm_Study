'''
https://www.acmicpc.net/problem/13549
제목 : 숨바꼭질 3

문제)
- 

수빈이 동생과
'''
import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100001 # 방문 시간 기록 

def bfs():
    q = []
    heapq.heappush(q, (0, N)) # (시간, 위치)
    visited[N]= 0

    while q:
        t, now = heapq.heappop(q)
        if now == K:
            return t

        # 순간이동 처리 (시간이 늘어나지 않음)
        next = now * 2
        if 0 <= next <= 100000 and (visited[next] == -1 or visited[next] > t):
            visited[next] = t
            heapq.heappush(q, (t, next))
        
        # 걷기 처리 (-1과 +1, 1초 소요)
        for next in (now - 1, now + 1):
            if 0 <= next <= 100000 and (visited[next] == -1 or visited[next] > t + 1):
                visited[next] = t + 1
                heapq.heappush(q, (t + 1, next))

print(bfs())