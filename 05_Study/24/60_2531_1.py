"""
https://www.acmicpc.net/problem/2531
제목: 회전 초밥

문제)
- 회전하는 벨트 위에 여러 번호의 초밥이 놓여져 있음
- 초밥 종류를 번호로 표현
- 같은 종류의 초밥이 둘 이상 있을 수 있음

- [ 행사 내용 ]
    - 회전 초밥은 손님이 마음대로 고르고 \
      임의의 한 위치 부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
    - 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행 \
      1번 행사에 참가할 경우 이쿠폰에 적혀진 종류의 초밥을 추가로 무료로 제공
      만약 이 번호 초밥이 현재 회전 초밥에 없을 경우, 요리가사가 새로 만들어 제공

- 예시
    - [7, 9, 7, 30, 2, 7, 9, 25] : 회전 초밥
    - k=4이고, 쿠폰번호가 30인경우
    - 쿠폰을 고려하지 않으면 4가지 다른 초밥 경우
        - (9, 7, 30, 2)
        - (30, 2, 7, 9)
        - (2, 7, 9, 25)
    - 30번 초밥을 추가로 쿠폰으로 먹을 수 있으므로 (2, 7, 9, 25)를 고르면 5가지 종류의 초밥

- 회전 초밥 음식점의 벨트 상태, 메뉴에 있는 초밥의 가짓수, 연속해서 먹는 접시의 개수, 쿠폰 번호가 주어졌을 때, 손님이 먹을 수 있는 초밥 가짓수의 최댓값을 구하는 프로그램

입력 예시 1)
8 30 4 30 : 접시수N, 초밥가짓수d, 연속접시수k, 쿠폰번호c
7         : 회전초밥 번호 (8줄)
9
7
30
2
7
9
25


브루트포스 알고리즘
두 포인터
슬라이딩 윈도우
"""

import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

sushi += sushi[:k-1] # 원형으로 생각하기 위해 추가 

max_sushi = 0

l = 0
r = k

for i in range(N):
    temp_set = set(sushi[l:r])
    temp_len = len(temp_set)
    if c not in temp_set:
        temp_len += 1
    max_sushi = max(max_sushi, temp_len)
    l += 1
    r += 1

print(max_sushi)


"""
O(N * k) : 매번 set 생성
"""



