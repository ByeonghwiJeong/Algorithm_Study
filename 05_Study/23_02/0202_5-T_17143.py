'''
< 낚시왕 >
https://www.acmicpc.net/problem/17143
문제)
- 낚시를 하는곳 : R x C (2 <= R, C <= 100)
- (R, C) : 가장 오른쪽 아래
- 한 칸에 상어는 최대 1마리, 상어는 크기와 속도를 가짐
- 낚시왕은 1번열 한 칸 왼쪽에 있다.
- 1초 동안 일어나는 일, 가장오른쪽 열의 오른쪽칸에 도달시 끝
    - 1. 낚시왕이 오른쪽으로 한 칸 이동
    - 2. 낚시왕이 있는 열에 있는 상어 중 땅과 제일 가까운 상어를 잡는다.
    - 3. 상어가 이동한다.
- 상어는 입력으로 주어진 속도로 이동 (칸/초)
- 상어가 경계 넘는경우 반대방향으로 속력 유지
- 상어가 이동을 마친 후 한 칸에 상어가 두 마리 이상 가능
    - 크기가 가장 큰 상어가 나머지 상어를 잡아먹는다.
- 낚시왕이 잡은 상어 크기의 합
입력)
- 1    : R, C, M (상어의 수)
- 2    : r, c, s, d, z (상어의 정보)
       - r, c : 상어의 위치
       - s    : 속력
       - d    : 이동방향 (1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽)
       - z    : 크기
출력)
- 낚시왕이 잡은 상어 크기의 합
'''
import sys, copy
input = sys.stdin.readline

R, C, M = map(int, input().split())
sea = [[0] * C for _ in range(R)]
# 위, 아래, 오른쪽, 왼쪽
dr = (-1, 1, 0, 0)
dc = (0, 0, 1, -1)
# index 1부터 시작 : sea에서 index로 상어 표시
# shark = [0] # 상어 정보 
shark = [[0, 0, 0, 0, 0, 0] for _ in range(R * C + 1)] # 상어 정보
for i in range(1, M + 1): 
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    if d <= 1: s %= 2 * (R - 1)
    else: s %= 2 * (C - 1)
    # shark.append([r, c, s, d, z, 0]) # 마지막 요소 : 죽음 여부
    # shark[i] = [r, c, s, d, z, 0] # 마지막 요소 : 죽음 여부
    shark[i][0] = r
    shark[i][1] = c
    shark[i][2] = s
    shark[i][3] = d
    shark[i][4] = z
    shark[i][5] = 0
    sea[r][c] = i
# print(*shark, sep='\n')

ret = 0 # 상어 크기의 합
for t in range(C): #사람이 움직임
    for y in range(R): # 상어를 잡음
        if sea[y][t]: # 상어가 있는경우
            shark[sea[y][t]][5] = 1 # 상어가 죽음(정보)
            ret += shark[sea[y][t]][4] # 상어 크기의 합
            sea[y][t] = 0 # 상어가 죽음(바다)
            break # 한마리만

    tmp = [[0] * C for _ in range(R)] 
    for j in range(1, M + 1): # 상어가 움직임
        if shark[j][5]: continue # 상어가 죽은경우
        r, c, s, d = shark[j][:4] # 중간변수를 미리 선언
        # 벽에 두번 부딪히는 경우
        while True:
            nr = r + s * dr[d]
            nc = c + s * dc[d]
            if 0 <= nr < R and 0 <= nc < C: break 
            if d <= 1: # 상하
                if nr < 0: s -= r; r = 0
                else: s -= R - 1 - r; r = R - 1
            else: # 좌우
                if nc < 0: s -= c; c = 0
                else: s -= C - 1 - c; c = C - 1
            d ^= 1 # 반대방향
        
        if tmp[nr][nc]:
            if shark[tmp[nr][nc]][4] < shark[j][4]:
                shark[tmp[nr][nc]][5] = 1
                tmp[nr][nc] = j
            else: shark[j][5] = 1
        else: tmp[nr][nc] = j

        # shark[j][:4] = [nr, nc, s, d] # s???
        shark[j][0] = nr
        shark[j][1] = nc
        shark[j][3] = d
    sea = copy.deepcopy(tmp)
print(ret)



'''
구현 문제
1. 사람이 움직임
2. 상어를 잡음
3. 상어가 움직임
4. 상어 잡아먹음

일반적으로 3번로직에서 시간초과가 발생
- 모듈러 연산을 통해서 한칸씩 이동이 아닌 한번에 이동
0  1  2  3  4  | C = 5 | 10칸 - 5 + (5-2)

다음위치 = (현재위치 + 10) % 2(C-1) # 0 ~ 7
         = 10 % 8 = 2

모듈러 연산이 들어가면 좌표시작을 0으로 하자!!!
1  2  3  4 을 모듈연산하면 1  2  3  0 이 되므로
0  1  2  3 으로 시작하자

문제에서 주어진 방향벡터는 (1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽)
그러나 문제를 수월하게 풀기위해서
(0: 위, 1: 아래, 2: 오른쪽, 3: 왼쪽)으로 변경하자
방향 전환시 XOR 연산자를 사용하기 위해서
0    1    2   3
00   01   10  11
0 => 1 : 00 ^ 01 = 01
1 => 0 : 01 ^ 01 = 00
2 => 3 : 10 ^ 01 = 11
3 => 2 : 11 ^ 01 = 10

중간에 실수를 방지하기 위해서 중간변수 선언

< 벽에 두번 부딪히는 경우 > C = 5
[ ][ ][O][ ][ ] : 위치 2, 왼쪽방향 속도 7
[O][ ][ ][ ][ ] : 위치 0, 오른쪽방향 속도 5
[ ][ ][ ][ ][O] : 위치 4, 왼쪽방향 속도 1
[ ][ ][ ][O][ ] : 위치 3, 최종 위치
'''