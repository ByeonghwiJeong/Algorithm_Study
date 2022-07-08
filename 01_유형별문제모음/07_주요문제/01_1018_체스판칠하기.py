'''
50 * 50
M N이 가장 큰경우
43 * 43 = 1849
체스판 W B 두가지로 시작하는경우로 스캔
64 * 2
236672 <<< 시간 제한 2초 = 2억

[[완전 탐색 가능함]]
'''
N, M = map(int, input().split())
board = [input() for _ in range(N)]

def fill_cnt(y, x):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0: #짝수
                if board[y+i][x+j] != 'B':
                    cnt += 1
            else: #홀수 
                if board[y+i][x+j] == 'B':
                    cnt += 1
    return min(cnt, 64-cnt)
ans = 64
for i in range(N-7):
    for j in range(M-7):
        tmp_cnt = fill_cnt(i, j)
        if tmp_cnt < ans:
            ans = tmp_cnt
print(ans)