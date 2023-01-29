'''
< N번째 큰 수>
https://www.acmicpc.net/problem/2075
문제)
- N x N 표에 수가 채워져있다.
- 몇번째로 큰수를 찾는다.
'''
import sys, heapq
input = sys.stdin.readline

N = int(input())

hq = []
for _ in range(N):
    a = list(map(int, input().split()))
    for i in a:
        if len(hq) < N :
            heapq.heappush(hq, i)
        else:
            if hq[0] < i:
                heapq.heappop(hq)
                heapq.heappush(hq, i)
print(hq[0])

'''
1. 우선순위 큐안에 들어있는 원소의 개수가 N개 미만
    => 큐에 집어 넣는다.
2. N개라면
    1) 숫자가 최솟값보다 작거나 같은 경우 => pass
    2) 큰경우 최솟값을 빼고
'''