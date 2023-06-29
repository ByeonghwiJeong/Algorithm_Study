'''
2차원 격자
격자에 존재하는 모든 도형이 차지하는 면적
격자에 있는 도형의 정의
1. '#'을 기준으로 상하좌우 대각으로 인접한 '#'이 있다면,\
        두 '#'을 연결하는 선을 긋습니다.
2. 선을 이루는 '#'과 선으로 둘러싸인 '#'과 '.'은 도형을 이룹니다.
3. 1 x 1 모양이나 선으로만 이루어진 형태도 도형이라 판단
4. 도형이 차지하는 면적은 도형에 포함되어있는 '#'의 개수 \
        도형 내부에 존재하는 '#'과 '.'의 개수
'''
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c, visited, f, tmp, R, C):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if visited[nr][nc]: continue
    
            visited[nr][nc] = 1
            tmp.append((nr, nc))
            dfs(nr, nc, visited, f, tmp, R, C)
        else:
            f = False

def solution(grid):
    global ret
    C = len(grid[1])
    R = len(grid)
    grid = [list(x) for x in grid]
    visited = [[0] * C for _ in range(R)] 
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '#': continue
            if visited[i][j]: continue
            flag = True
            tmp = [(i, j)]
            visited[i][j] = 1 
            dfs(i, j, visited, flag, tmp, R, C)
            print(flag)
    answer = 0
    return answer

print(solution([
    ".....####", 
    "..#...###", 
    ".#.##..##", 
    "..#..#...", 
    "..#...#..", 
    "...###..."]))