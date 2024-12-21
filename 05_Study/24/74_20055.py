"""
https://www.acmicpc.net/problem/20055
제목: 컨베이어 벨트 위의 로봇

문제)
- 길이가 N인 컨베이어 벨트
- 길이가 2N인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있다
- 1부터 2N까지의 번호
- 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호의 칸이 있는 위치로 이동하고, 2N번 칸은 1번 칸의 위치로 이동
- 박스 모양 로봇을 하나씩 올리려고 한다. 로봇은 올리는 위치에만 올릴 수 있다
- 로봇은 컨베이어 벨트 위에서 스스로 이동
- 봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소
- 로봇을 옮기는 과정에서는 아래와 같은 일이 순서
    1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다
        (로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 함)
    3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

입력)
첫째 줄에 N, K가 주어진다. 둘째 줄에는 A1, A2, ..., A2N이 주어진다.
출력)
몇 번째 단계가 진행 중일 때 종료되는지 출력
"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
belts = deque(map(int, input().split()))
robots = deque([0]*N*2) # 0: 로봇 없음, 1: 로봇 있음

step = 0
count = 0 # 내구도가 0인 칸의 개수

while count < K:
    step += 1
    # 1. 벨트 회전
    belts.rotate(1)
    robots.rotate(1)
    robots[N-1] = 0 # 내리는 위치에 로봇이 있으면 내림

    # 2. 로봇 이동 (앞부터)
    for i in range(N-2, -1, -1): # N-2 ~ 0
        if not robots[i]: continue # 로봇이 없으면 패스
        if robots[i+1]: continue # 다음 칸에 로봇이 있으면 패스
        if not belts[i+1]: continue # 다음 칸의 내구도가 0이면 패스
        robots[i] = 0
        robots[i+1] = 1
        belts[i+1] -= 1
        if not belts[i+1]: # 내구도가 0이면
            count += 1

    # 내리는 위치에 로봇이 있으면 내림
    robots[N-1] = 0
    # 3. 로봇 올리기
    if belts[0]: # 올리는 위치의 내구도가 0이 아니면 로봇 올림
        robots[0] = 1
        belts[0] -= 1
        if not belts[0]:
            count += 1

print(step)
    
        

