'''
눈금 간격이 M x N 크기의 모눈종이가 있다.
이 모눈종이 위에 K개의 직사각형을 그린다.
K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리 된 영역으로 나누어진다.

입력)
    - 1 : M, N, K ~ [1, 100]자연수
    - 2 : K개의 줄에 하나씩 직사각형의 대각 꼭짓점이 주어진다. - 꼭짓점이라서 -1 해야함(range에서는 x)

출력)
    - 1 : 영역의 갯수
    - 2 : 그 영역의 넓이 오름차순

좌표계의 순서가 매우 어지러움
'''
M, N, K = map(int, input().split())
_board = [[1] * N for _ in range(M)]
_check = [[True] * N for _ in range(M)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def rec_check(r1, c1, r2, c2):
    for i in range(r1, r2):
        for j in range(c1, c2):
            try:
                _board[i][j] = 0
            except:
                print(i, j)
                exit(0)

for _ in range(K):
    # 좌표랑 row col 반대주의!
    c1, r1, c2, r2 = map(int, input().split())
    rec_check(r1, c1, r2, c2)


def coord_vaild(r, c):
    # 표안에 있는지
    if 0<= r < M and 0 <= c < N:
        # board값이 1이고(0x) check가 True
        if _check[r][c] and _board[r][c]:
            return True
    return False

area = []
cnt = 0
def dfs(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
         



for i in range(M):
    for j in range(N):
        if coord_vaild(i, j):
            _check[i][j] = False
            cnt += 1
            dfs(i, j)

