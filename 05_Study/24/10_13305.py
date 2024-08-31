'''
https://www.acmicpc.net/problem/13305
제목 : 주유소

문제)
- 도시 N개가 있다
- 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동
- 1리터의 기름으로 1km 이동 가능
- 각 도시에는 단 하나의 주유소가 있으며 도시마다 주유소의 리터당 가격이 다르다

입력)
- 1    : N ~ [2, 100_000]
- 2    : N개의 도시를 연결하는 도로의 길이
- 3    : N개의 도시의 주유소 가격

ex input)
4
2 3 1
5 2 4 1
ex output)
18
'''
import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

total_cost = 0
min_price = price[0]

for i in range(N-1):
    if price[i] < min_price:
        min_price = price[i]
    total_cost += min_price * dist[i]


print(total_cost)