'''
< 줄 세우기 > 
https://www.acmicpc.net/problem/2252
문제) 
- N명의 학생들을 키 순서대로 줄세우려고 한다.
- 일부 학새의 키만 비교
입력)
- 1     : N ~ [1 \ 32,000], M ~ [1 \ 100,000]
- 2     : A, B ~ 학생A가 학생B의 앞에 서야 한다.
출력)
- 
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    ret = []
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        ret.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0: q.append(i)
    return ret
print(*topology_sort())
