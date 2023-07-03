"""
https://school.programmers.co.kr/learn/courses/30/lessons/68645

! 접근)
* 1. n x n 2차원배열
* 2. 반시계 방향의 나선형으로 배열을 채워나감
* 3. 배열의 끝에 닿거나 할당값이 있으면 방향전환
* 4. 마지막 할당
"""

def solution(n):
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    snail = [[0] * i for i in range(1, n + 1)]
    r = c = angle = 0
    cnt = 1
    size = (n + 1) * n // 2

    while cnt <= size:
        snail[r][c] = cnt 
        nr = r + dr[angle]
        nc = c + dc[angle]
        cnt += 1

        if 0 <= nr < n and 0 <= nc < n and  snail[nr][nc] == 0:
            r, c = nr, nc
        else:
            angle = (angle + 1) % 3
            r += dr[angle]
            c += dc[angle]
        
    return [i for j in snail for i in j]