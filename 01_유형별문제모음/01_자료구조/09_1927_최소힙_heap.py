'''
자료구조 최소힙
1. 배열에 자연수 x 넣기
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거
입력)
    - N : 연산의 개수
    - 정수 x (N번)
        - 자연수 x : x 넣기
        - x == 0 : 가장 작은값 출력

'''
import sys, heapq
input = sys.stdin.readline

_list = []

'''
for i in range(int(input())):
    x = int(input())
    if x == 0:
        print(heapq.heappop(_list) if len(_list) > 0 else 0)
    else:
        heapq.heappush(_list, x)
'''
cals = []
for _ in range(int(input())):
    cals.append(int(input()))

heapq.heapify(_list)
for c in cals:
    if c:
        heapq.heappush(_list, c)
    else:
        if _list:
            print(heapq.heappop(_list))
        else:
            print(0)