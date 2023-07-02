"""
https://school.programmers.co.kr/learn/courses/30/lessons/87377
접근)
- 1. 주어진 직선에서 교점을 찾는다.
- 2. 정수 교점을 저장
- 3. 교점을 기준으로 사각형을 알아냄
- 4. 배열을 뒤집어서 반환

교점 구하는 방법)
Ax + By + E = 0
Cx + Dy + F = 0
x = (BF - ED) / (AD - BC)
y = (EC - AF) / (AD - BC)
"""

def solution(line):
    pos = list()

    x_min = y_min = float('inf')
    x_max = y_max = float('-inf')

    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            if a * d == b * c: continue
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            if x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                pos.append((x, y))
                x_min = min(x_min, x)
                x_max = max(x_max, x)
                y_min = min(y_min, y)
                y_max = max(y_max, y)

    width = x_max - x_min + 1
    height = y_max - y_min + 1
    answer = [["."] * width for _ in range(height)]

    for star_x, star_y in pos:
        nx = star_x - x_min
        ny = y_max - star_y # y 는 역순이므로
        answer[ny][nx] = '*'

    return list(map("".join, answer))


