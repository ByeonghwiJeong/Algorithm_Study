'''
N x N 행렬 각 칸에 -1 0 1 중 하나 저장
1. 종이가 모두 같은 수이면 그 종이를 사용
2. -1의수 0의수 1의수

_dict 선언 순서에 따라서 error 발생 global 상관x 
'''
import sys
input = sys.stdin.readline

_dict = {-1 : 0, 0 : 0, 1 : 0}

def chk(r, c, n):
    for i in range(r, r + n):
        for j in range(c, c + n):
            if _board[i][j] != _board[r][c]:
                return False
    return True

def recur(r, c, n):
    global _dict, _board
    if chk(r, c, n):
        _dict[_board[r][c]] += 1
        return

    t = n // 3
    for i in range(3):
        for j in range(3):
            recur(r + i*t, c + j*t, t)
    return 

N = int(input())
_board = [list(map(int, input().split())) for _ in range(N)]
recur(0, 0, N)
print(*_dict.values(), sep='\n')