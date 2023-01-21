'''
< 컨베이어 벨트 위의 로봇 > 
https://www.acmicpc.net/problem/20055
문제)
- 길이 N인 컨베이어 벨트가 있고, \
    길이가 2N인 벨트가 이 컨베이어 벨트를 위 아래로 감싸며 돌고 있다.
- 각 칸에는 아래 그림과 같이 1부터 2N까지의 번호가 매겨져 있다.
- i번째칸의 내구도 Ai
- 벨트가 회전시
    - 1 ~ 2N-1 : + 1
    - 2N       : 1
- 1번칸이 있는 위치 : 올리는 위치
- N번칸이 있는 위치 : 내리는 위치
- 컨베이어 벨트에 박스 모양 로봇을 하나씩 올리려고한다.
    - 올리는 위치에만 올릴 수 있다.
    - 내리는 위치에 도달하면 그 즉시 내린다.
- 로봇은 컨베이어 벨트에서 이동가능
    - 올리는 위치에 올리거나 어떤 칸으로 이동하면 그 칸의 내구도 1감소
- 컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려고 한다.
- < 로봇을 옮기는 과정 >
    - 1. 벨트가 각 칸위에 있는 로봇과 함께 한 칸 회전
    - 2. 가장 먼저 벨트에 올라간 로봇 부터 벨트가 회전하는 방향으로 한칸 이동가능시 이동
        ( 이동하려는 칸에 로봇X, 그 칸의 내구도가 1이상 남아 있어야한다. )
    - 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    - 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
- 종료되었을 때 몇 번째 단계가 진행 중이었는지 구하자 \
    (가장 처음 수행 되는 단계는 1번째 단계이다)
입력)
- 1     : N, K
- 2     : A1, A2, ... A2n
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([False] * 2 * n) # 로봇존재 Check
# 로못 올리는 위치 0, 내리는 위치 1
step = 0
count = 0 # 내구도가 0인 칸의 수
while True:
    step += 1
    # 1. 회전
    robots.rotate(1)
    belt.rotate(1)
    robots[n-1] = False # 로봇 내리기
    # 2. 로봇 이동 (앞부터)
    for i in range(n-2, -1, -1): # idx : n-2 ~ 0
        if not robots[i]: continue # 로봇 없는경우
        if robots[i + 1]: continue # 다음칸에 로봇 있는경우
        if belt[i+1] == 0: continue # 다음칸 내구도 0인경우
        robots[i] = False
        robots[i + 1] = True
        belt[i + 1] -= 1
        if belt[i + 1] == 0: count += 1
    # 내리는 위치에 로봇이 옮겨진 경우 바로 내리기
    robots[n - 1] = False
    # 3. 로봇 올리기
    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1
        if belt[0] == 0: count += 1
    
    if count >= k: break

print(step)
