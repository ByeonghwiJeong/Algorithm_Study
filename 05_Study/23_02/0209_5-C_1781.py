'''
< 컵라면 >
https://www.acmicpc.net/problem/1781
문제)
- 상욱조교는 동호에게 N개의 문제를 준다.
- 각각의 문제를 풀었을 때 컵라면을 몇 개 줄 것인지 제시
- 데드라인 존재
- 동호가 받을 수 있는 최대 컵라면 수???
입력)
- 1     : 숙제의 개수 N ~ [1 \ 200,000]
- 2[N]  : 데드라인 컵라면

'''
import sys, heapq
input = sys.stdin.readline

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
a.sort()
hq = []
ret = 0
for i in range(N):
    ret += a[i][1]
    heapq.heappush(hq, a[i][1])
    if len(hq) > a[i][0]:
        ret -= heapq.heappop(hq)
print(ret)

'''
### 문제에는 데드라인이 있음 - 구간안에 풀어야함!!!
- 라인스위핑
[라인스위핑](https://blog.kakaocdn.net/dn/biuYDc/btrrpEpHCiq/iOCbtB5hkcYMmtt9NEqwW0/img.png)
'''