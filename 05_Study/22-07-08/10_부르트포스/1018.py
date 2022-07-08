'''
M x N 크기의 정사각형으로 이루어져 있는 보드에 대하여
 -  어떤 정사각형은 검은색으로 칠해져 있고,
 -  나머지는 흰색으로 칠해져 있다.
이보드 판을 8 x 8 크기의 체스판으로 만들려고 한다.

1. 가로 세로를 각각 M-7 x N-7 탐색한다.
2. 탐색위치에서 시작이 W인경우와 B인경우를 구분하고 최소 값을 반환

'''

N, M = map(int, input().split())
board = [ input() for _ in range(N) ]

# print(board)
def check_wb(y, x):
    cnt = 0
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            # print(cnt)
            if (i + j) % 2 == 0: # 짝수인 경우
                if board[i][j] == 'B': 
                    cnt += 1
            else: # 홀수
                if board[i][j] != 'B':
                    cnt += 1
    # 시작한 체스판 W / B 
    return min(cnt, 64-cnt)

ans = float('inf')
for i in range(N-7):
    for j in range(M-7):
        tmp_min = check_wb(i, j)
        if tmp_min < ans:
            ans = tmp_min
# print('-----------')
# print(check_wb(0, 0))
print(ans)