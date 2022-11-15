'''
실패실패실패실패실패실패실패실패실패실패실패실패
'''
from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
a = list(map(int, input().split()))
q = a[:]
cnt = n
while cnt:
    temp = []
    for i in a:
        for j in q[-k:]:
            temp.append(i*j)
    q += temp
    cnt -= 1
q.sort()
print(q)
print(q[n-1])