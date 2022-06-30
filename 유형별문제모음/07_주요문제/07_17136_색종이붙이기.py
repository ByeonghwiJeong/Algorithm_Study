'''
정사각형 모양의 1^2 2^2 3^3 4^2 5^2 다섯 종류가 있으며, 
각 종류의 색종이는 5개씩 가지고 있다.

색종이를 크기가 10 x 10 종이 위에 붙이려고 한다.
종이는 1 x 1 크기의 칸으로 나누어져 있으며, 
각각의 칸에는 0또는 1이 적혀있다.
1이 적힌 칸은 모두 색종이로 덮여져야한다.
0이 적현 칸은 색종이가 있으면 안된다.

경계 밖으로 나가서는 안되고, 겹쳐도 안 된다.
또 경계와 일치하게 붙어야 한다.

종이가 주어졌을 때 1이 적힌 모든칸을 붙이는데 필요한 색종이의 최소 개수를 구해보자.

8 x 8 색종이를 5 x 5를 이용하는것보다 4 x 4 를 이용하는게 더 최소이다.


[[ 백트레킹 ]]


'''
board = [list(map(int, input().split())) for _ in range(10)]
ans = 25
paper = [0] * 6
# 사용한 색종이 개수 ( 크기 1 ~ 5)

def is_possible(y, x, sz):
    if paper[sz] == 5: # 이미 5장 사용한경우 x
        return False
    if y + sz > 10 or x + sz > 10: # 경계선 넘어선경우
        return False
    for i in range(sz):
        for j in range(sz):
            if board[y + i][x + j] == 0:
                return False
    return  True

def mark(y, x, sz, v):
    for i in range(sz):
        for j in range(sz):
            board[y + i][x + j] = v

    if v: # 1 >> 색종이를 제거한경우
        paper[sz] -= 1
    else: # 0 >> 색종이를 사용한경우
        paper[sz] += 1


def backtracking(y, x):
    global ans
    if y == 10:
        ans = min(ans, sum(paper))
        return
    if x == 10:
        backtracking(y + 1, 0)
        return
    if board[y][x] == 0:
        backtracking(y, x +  1)
        return
    
    for sz in range(1, 6):
        if is_possible(y, x, sz):
            mark(y, x, sz, 0)
            backtracking(y, x + 1)
            mark(y, x, sz, 1) #원상복구 

backtracking(0, 0)
print(-1 if ans == 25 else ans)