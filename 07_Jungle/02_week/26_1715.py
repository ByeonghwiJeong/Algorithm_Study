'''
< 카드 정렬하기 >
https://www.acmicpc.net/problem/1715
문제)
- 정렬된 두 묶음의 숫자카드가 있다.
- 각 묶음의 카드의 수를 A, B라 한다.
- A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는데에 \
    A + B 번의 비교를 해야한다.
- 
입력)
- 
출력)
-
'''
import sys, heapq
input = sys.stdin.readline

n = int(input())
hq = [int(input()) for _ in range(n)]
heapq.heapify(hq)
ret = 0
if n == 1:
    print(0)
    sys.exit(0)
while True:
    temp = heapq.heappop(hq) + heapq.heappop(hq)
    ret += temp
    if len(hq) == 0: break
    heapq.heappush(hq, temp)
print(ret)

