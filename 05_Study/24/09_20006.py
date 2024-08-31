'''
https://www.acmicpc.net/problem/20006
제목 : 랭킹전 대기열

문제)
- 플레이어간 매칭 시스템
1. 매칭 가능한 방이 없으면 새로운방 생성 & 입장 (해당방은 -10 ~ +10 허용)
2. 입장 가능한 방이 있으면 입장시킨 후 방의 정원이 모두 찰 때까지 대기
  - 입장 가능한 방이 여러개면 가장 먼저 생성된 방에 입장
3. 방의 정원이 모두 차면 게임 시작
- 플레이어의 수 p, 플레이어의 닉네임 n, 플레이어의 레벨 l, 방의 최대 인원 m

입력)
- 1    : p ~ [1, 300], m ~ [1, 300]
- 2 [p]: l n

출력)
모든 생성된 방에 대해서 게임의 시작 유무와 방에 들어있는 플레이어들의 레벨과 아이디를 출력한다. 시작 유무와 플레이어의 정보들은 줄 바꿈으로 구분되며 레벨과 아이디는 한 줄에서 공백으로 구분된다.
방은 생성된 순서대로 출력한다.
방에 있는 플레이어들의 정보는 닉네임이 사전순으로 앞서는 플레이어부터 출력한다.
방이 시작되었으면 Started!를 대기 중이면 Waiting!을 출력시킨다.

10 5
10 a
15 b
20 c
25 d
30 e
17 f
18 g
26 h
24 i
28 j

Started!
10 a
15 b
20 c
17 f
18 g
Started!
25 d
30 e
26 h
24 i
28 j
'''
P, M = map(int, input().split())
players = [input().split() for _ in range(P)]
players = [(int(l), n) for l, n in players]  # 레벨을 정수로 변환
rooms = []

# 플레이어를 방에 배정
for l, n in players:
    matched = False
    for room in rooms:
        # 방이 아직 꽉 차지 않았고 레벨 범위가 맞는 방에 입장
        if len(room) < M and room[0][0] - 10 <= l <= room[0][0] + 10:
            room.append((l, n))
            matched = True
            break
    # 입장할 방이 없다면 새 방 생성
    if not matched:
        rooms.append([(l, n)])

# 출력
for room in rooms:
    room.sort(key=lambda x: x[1])  # 닉네임 기준으로 정렬
    if len(room) == M:
        print('Started!')
    else:
        print('Waiting!')
    for lv, name in room:
        print(lv, name)
