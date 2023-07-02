"""
https://school.programmers.co.kr/learn/courses/30/lessons/77485
접근)
- 1. 1씩 증가하는 행렬을 생성합니다.
- 2. 회전해야 할 위치들의 값을 받아옵니다.
- 3. 행렬을 시계 방향으로 회전시킵니다.
- 4. 3번 과정에서 최솟값을 찾습니다.
"""

def rotate(x1, y1, x2, y2, matrix):
    first = matrix[x1][y1]
    min_value = first

    # 왼쪽
    for i in range(x1, x2):
        matrix[i][y1] = matrix[i+1][y1]
        min_value = min(min_value, matrix[i+1][y1])
    # 아래
    for i in range(y1, y2):
        matrix[x2][i] = matrix[x2][i+1]
        min_value = min(min_value, matrix[x2][i+1])
    # 오른쪽
    for i in range(x2, x1, -1):
        matrix[i][y2] = matrix[i-1][y2]
        min_value = min(min_value, matrix[i-1][y2])
    # 위
    for i in range(y2, y1, -1):
        matrix[x1][i] = matrix[x1][i-1]
        min_value = min(min_value, matrix[x1][i-1])
    
    matrix[x1][y1+1] = first
    return min_value

def solution(rows, columns, queries):
    matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    result = []
    for x1, y1, x2, y2 in queries: # x:row, y:col
        result.append(rotate(x1-1, y1-1, x2-1, y2-1, matrix))
    return result