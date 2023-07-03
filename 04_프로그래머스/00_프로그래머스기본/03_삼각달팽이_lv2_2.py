"""
? https://school.programmers.co.kr/learn/courses/30/lessons/68645

! 접근)
* 1. n x n 2차원배열
* 2. 반시계 방향의 나선형으로 배열을 채워나감
* 3. 배열의 끝에 닿거나 할당값이 있으면 방향전환
* 4. 마지막 할당
"""

def solution(n):
    result = [[0] * i for i in range(1, n + 1)]
    r, c = -1, 0 # 처음 시작고려해서 -1 시작
    num = 1

    for i in range(n): # n = 4 >>> (0, 1, 2, 3)
        direction = i % 3
        for _ in range(i, n): # 0, 1, 2, 3 // 0, 1, 2 // 0, 1
            if direction == 0: r += 1
            elif direction == 1: c += 1
            elif direction == 2: r -= 1; c -= 1
            result[r][c] = num
            num += 1
        
    return [i for j in result for i in j]