'''
< 숨바꼭질3 > 
https://www.acmicpc.net/problem/13549
문제)
- 수빈이는 동생과 숨바꼭질을 하고 있다.
- 수빈이는 현재 점 N ~ [0 \ 100,000]
- 동생은 현재 점 K ~ [0 \ 100,000]
- 수빈이는 걷거나 순간이동 가능
    - 걷기 : 1초후 X-1 or X+1
    - 순간이동 : 0초후 2*X
- 수빈이가 동생을 찾는 가장 빠른 시간이 몇 초 후인지???
입력)
- 1     : N, K
'''
import sys, heapq as hq
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * 100001

def bfs():
    q = []
    hq.heappush(q, (0, n))
    visited[n] = 1
    while q:
        t, now = hq.heappop(q)
        if now == k: return t
        next = now * 2
        if 0 <= next <= 100000:
            if not visited[next]: 
                visited[next] = 1
                hq.heappush(q, (t, next))
        for next in (now - 1, now + 1):
            if 0 <= next <= 100000:
                if visited[next]: continue
                visited[next] = 1
                hq.heappush(q, (t + 1, next))
    return

print(bfs())
print(visited[1])