"""
https://acmicpc.net/problem/11501

제목 : 주식

문제)
- 매일 그는 아래 세 가지 중 한 행동
    1. 주식 하나를 산다.
    2. 원하는 만큼 가지고 있는 주식을 판다.
    3. 아무것도 안한다.
- 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산


입력 예시 1)
3 - 테스트 케이스 수
3
10 7 6
3
3 5 9
5
1 1 3 1 2
출력 예시 1)
0
10
5
"""
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    stocks = list(map(int, input().split()))
    max_price = 0
    profit = 0

    for i in stocks[::-1]:
        if i > max_price:
            max_price = i
        else:
            profit += max_price - i

    print(profit)