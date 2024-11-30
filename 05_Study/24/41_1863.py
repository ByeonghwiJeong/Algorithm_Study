'''
https://acmicpc.net/problem/1863
제목 : 스카이라인 쉬운거

문제)
- 스카이라인만을 보고 도시에 세워진 건물의 개수를 구하라
- 건물은 모두 직사각형
- 정확히 건물이 몇개 있는지는 대부분 불가능하고, 건물이 최소한 몇 채 인지 알아내는 것은 가능

입력)
- 1   : n ~ [1, 50_000] n개의 줄
- 2[n]: 스카이라인의 고도가 바뀌는 지점의 좌표 x, y ~ [1, 1_000_000]

출력)
- 건물의 최소 개수

입력 예시)
10
1 1
2 2
5 1
6 3
8 1
11 0
15 2
17 3
20 2
22 1

출력 예시)
6


입력은 다음과 같은 스카이라인을 나타낸다.

..........................
.....XX.........XXX.......
.XXX.XX.......XXXXXXX.....
XXXXXXXXXX....XXXXXXXXXXXX
다음과 같이 여섯 개의 빌딩이 있을 때가 최소 개수의 빌딩이 있는 상황이다.

..........................
.....22.........333.......
.111.22.......XX333XX.....
X111X22XXX....XX333XXXXXXX

..........................
.....XX.........XXX.......
.XXX.XX.......5555555.....
4444444444....5555555XXXXX

..........................
.....XX.........XXX.......
.XXX.XX.......XXXXXXX.....
XXXXXXXXXX....666666666666
'''
import sys
input = sys.stdin.readline

n = int(input())
pos_list = [list(map(int, input().split())) for _ in range(n)]

stack = [0]  # 처음에 0을 넣고 시작 (! 중요)
result = 0

for _, y in pos_list:
    # 스택의 top이 현재 높이 y보다 크면, pop 하면서 건물의 끝을 처리
    while stack and stack[-1] > y:
        stack.pop()
        result += 1  # 건물의 끝을 만났으므로 result 증가

    # 스택이 비었거나, 현재 높이가 이전 높이보다 크면 새 건물 추가
    if stack[-1] < y:
        stack.append(y)

# 남아있는 스택이 있을 경우 건물이 종료되지 않은 상태이므로 pop 처리
while len(stack) > 1: 
    stack.pop()
    result += 1

print(result)