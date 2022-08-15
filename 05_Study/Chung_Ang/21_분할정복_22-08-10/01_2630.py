'''
함수 (x1, y1, x2, y2)
(0, 0) (7, 7)[8, 8] 
    (0, 0)(3, 3)[4, 4]
    (0, 4)(3, 7)[4, 8]
    (4, 0)(7, 3)[8, 4]
    (4, 4)(7, 7)[8, 8]
( )[ ]

.................dkdkdkddodkdkdkdk

r, c 로 해야 혼돈 XXX
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def check(x1, y1, x2, y2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            if board[y1][x1] != board[i][j]:
                # 
                return False
    return True

def recur(x1, y1, x2, y2):
    print(x1, y1, x2, y2)
    # 전체가 1 or 0 탐색
    # global board, wcnt, bcnt
    wcnt = 0
    bcnt = 0
    # tmp = board[x1][y1] # 1 or 0
    # flag = True

    # flag = check(x1, y1, x2, y2)

    if check(x1, y1, x2, y2):
        if board[y1][x1]: # 1
            # bcnt += 1
            return 0, 1
        else: # 0
            # wcnt += 1
            return 1, 0
    else:
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        # mx = x1 + N // 2
        a1, b1 = recur(x1, y1, mx, my) 
        # [0, 4) [0, 4)
        a2, b2 = recur(x1, my, mx, y2) # 
        a3, b3 = recur(mx, y1, x2, my)
        # [4, 8) 
        a4, b4 = recur(mx, my, x2, y2)
        wcnt += a1 + a2 + a3 + a4
        bcnt += b1 + b2 + b3 + b4
        return wcnt, bcnt

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(*recur(0, 0, N, N), sep='\n')

