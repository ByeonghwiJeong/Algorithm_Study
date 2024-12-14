"""
https://www.acmicpc.net/problem/25757
제목 : 임스와 함께하는 미니게임

문제)
- 임스는 같이할 사람을 찾고 있음
- 미니게임 : 윷놀이 Y, 같은 글미 찾기 F, 원가드 O
- 각 게임은 2, 3, 4명이서 할 수 있음
- 임스와 같이 플레이하기를 신청한 횟수 N과 임스가 플레이할 게임의 종류가 주어질 때,
    최대 몇 번이나 임스와 함께 게임을 플레이할 수 있는지 구하시오.
- 임스와 여러 번 미니겡미을 플레이하고자 하는 사람이 있으나, 임스는 한 번 같이 플레이한 사람과 다시 같이 플레이할 수 없음
- 동명이인 존재 X

입력)
7 Y           : N, 게임 종류
lms0806       : N줄 
lms0806
exponentiale
lms0806
jthis
lms0806
leo020630
"""
import sys
input = sys.stdin.readline
N, game = input().split()
game_max = {'Y': 2, 'F': 3, 'O': 4}
unique_people = {input().strip() for _ in range(int(N))}
print(len(unique_people) // (game_max[game] - 1))
