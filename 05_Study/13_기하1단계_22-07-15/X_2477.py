'''
특정 도형의 넓이구하기
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
동, 서, 남, 북 순서

코드가 너무 간결하지 못하다 개선해야함
'''
import sys
input = sys.stdin.readline

tmp_coord = [0, 0]
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]
X = [0]
Y = [0]
coords = []
N = int(input())
for _ in range(6):
    i, d = map(int, input().split())
    tmp_coord[0] += dx[i] * d
    tmp_coord[1] += dy[i] * d
    X.append(tmp_coord[0])
    Y.append(tmp_coord[1])
    coords.append((tmp_coord[0], tmp_coord[1]))
min_X = min(X)
max_X = max(X)
min_Y = min(Y)
max_Y = max(Y)
out_area = (max_X - min_X) * (max_Y - min_Y)
out_coords = [(min_X, min_Y), (max_X, max_Y), (max_X, min_Y), (min_X, max_Y)] 
in_coords = []
for i in coords:
    if not i in out_coords:
        in_coords.append(i)
# print(in_coords)
x = [i[0] for i in in_coords]
y = [i[1] for i in in_coords]
min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)
in_area = (max_x - min_x) * (max_y - min_y)
print(N * (out_area - in_area))