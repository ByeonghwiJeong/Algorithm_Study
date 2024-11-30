"""
https://www.acmicpc.net/problem/1244
제목: 스위치 켜고 끄기

문제)
- 1부터 연속적으로 번호가 붙어있는 스위치
- ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음
- 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어줌
- 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작
1. 남학생
    - 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태
    (스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다)
2. 여학생
    - 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간
    - 그 구간에 속한 스위치의 상태를 모두 바꾼다 
    - 구간에 속한 스위치 개수는 항상 홀수

    
입력 예시)
8               - 스위치 개수
0 1 0 1 0 0 0 1 - 스위치 상태
2               - 학생 수
1 3             - 학생 성별(1-남, 2-여), 받은 수
2 3
출력 예시)
1 0 0 0 1 1 0 1
"""


import sys
input = sys.stdin.readline

def toggle_switch(switches, index):
    switches[index] = 1 - switches[index]

def change_male(switches, num, total_switches):
    for i in range(num, total_switches + 1, num):
        toggle_switch(switches, i)

def change_female(switches, num, total_switches):
    toggle_switch(switches, num)
    left, right = num - 1, num + 1
    while left > 0 and right <= total_switches and switches[left] == switches[right]:
        toggle_switch(switches, left)
        toggle_switch(switches, right)
        left -= 1
        right += 1

def process_students(switches, students, total_switches):
    action_map = {
        1: change_male,
        2: change_female,
    }
    for gender, num in students:
        action_map[gender](switches, num, total_switches)


N = int(input())
switches = [0] + list(map(int, input().split()))
M = int(input())
students = [tuple(map(int, input().split())) for _ in range(M)]

process_students(switches, students, N)

for i in range(1, N + 1):
    print(switches[i], end=" ")
    if i % 20 == 0: 
        print()