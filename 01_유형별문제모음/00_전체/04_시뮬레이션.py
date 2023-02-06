"""
1. 아이디어
- while문으로, 특정조건 종료될떄까지 반복
- 4방향을 for문으로 탐색
- 더이상 탐색 불가능할경우, 뒤로 한칸 후진
- 후진이 불가능하면 종료
2. 시간복잡도
- O(NM) : 50^2 = 2500 < 2억
- 가능
3. 자료구조
- map : int[][]
- 로봇청소기 위치, 방향, 전체 청소한 곳 수

문제
https://www.acmicpc.net/problem/14503
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
#d가 0일때 북쪽 부터 시계방향
#index 기분 0 3 2 1 순

while 1:
  if map[y][x] == 0:
    map[y][x] = 2
    cnt += 1
  sw = False
  # print("d : ",d)
  for i in range(1,5):
    # print("d-i : ", d-i)
    ny = y + dy[d-i]
    nx = x + dx[d-i]
    
    if 0 <= ny < N and 0 <= nx < M:
      if map[ny][nx] == 0:
        d = (d-i)%4
        # 처음에 d = d - i로 할당했는데 위에 print를 찍어보니줌
        # d-i 값이 -5까지 갔다 %4를 추가해서 -5를 3으로 바꾸어줌
        y = ny
        x = nx
        sw = True
        break 
# 4방향 모두  있지 않은 경우
# break가 for문만들 나가서 4방향 모두 않은 경우에 실행
  if sw == False:
    #뒤쪽 막혀있는지 확인
    ny = y - dy[d]
    nx = x - dx[d]
    if 0 <= ny < N and 0 <= nx < M:
      if map[ny][nx] == 1:
        break
      else:
        y = ny
        x = nx
    else:
      break

print(cnt)