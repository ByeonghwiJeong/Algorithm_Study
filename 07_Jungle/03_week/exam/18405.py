'''
< 경쟁적 전염 > 
https://www.acmicpc.net/problem/18405
문제
- N x N 크기의 시험관
- 1 x 1 크기의 칸으로 나누어짐
- 특정위치에 바이러스, 1 ~ k번까지 바이러스

- 1초마다 4방향 증식
- 번호가 더 낮은 바이러스 먼저 증식
- 이미 바이러스 존재시 증식불가

입력)  
- 1     : N~[1 \ 200], K~[1 \ 1000]
- 2[N]  : N개의 줄에 걸쳐서 바이러스 정보
- 3     : s~[0 \ 10,000], x, y ~ [1 \ N]
출력)
- s초뒤에 (x, y)에서 바이러스 종류출력, 없으면 0
'''
from collections import deque
import sys
input = sys.stdin.readline 
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
s, r, c = map(int, input().split())

b = []
for i in range(n):
    for j in range(n):
        if not a[i][j]: continue
        b.append((a[i][j], i, j))
b.sort()
q = deque(b)
while s > 0:
    for _ in range(len(q)):
       x, sr, sc = q.popleft()
       for i in range(4):
            nr = sr + dr[i]
            nc = sc + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if a[nr][nc]: continue
                a[nr][nc] = x
                q.append((x, nr, nc))    
    s -= 1
print(a[r-1][c-1])