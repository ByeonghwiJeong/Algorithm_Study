'''
< 강의실 배정 >
문제)
- Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데,\
    최소의 강의실을 사용해서 모든 수업을 가능하게 해야한다.
- Ti <= Sj 인경우 i수업과 j수업을 들을 수 있다.
입력)
- 1     : N이 주어진다. ~ [1 \ 200,000]
- 2     : Si, Ti ~ [1 \ 10^9]
출력)
- 강의실의 개수
'''

import sys
import heapq as hq
input = sys.stin.readline

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort()
pq = [-1] # 처음 인덱스 에러 방지

for start, end in lectures:
    if pq[0] <= start: # 가장 빨리 긑나는 강의실을 사용할 수 있는경우
        hq.heappop(pq)
    hq.heappush(pq, end)

print(len(pq))

'''
- 강의실의 수를 최소로 하기 위해서, \
    현재 사용하는 강의실 중 빨리 끝나는 강의실에 가장먼저 시작하는 강의실을 배치
- 시작하는 순으로 정렬
- 가장 빨리 긑나느 시간을 구하기 위해 최소 힙(우선순위 큐) 사용
'''