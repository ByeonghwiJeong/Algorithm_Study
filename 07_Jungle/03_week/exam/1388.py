'''
< 바닥 장식 >
https://www.acmicpc.net/problem/1388
- 바닥 장식 디자인
- 나무 판자는 크기 1의 너비를 가졌고, 양수의 길이
- 기훈이 방은 직사각형 모양
- 방 안에는 벽과 평행한 모양의 정사각형으로 나누어 있다.

'-' '|' 으로 장식모양
두개의 '-'가 인접, 같은 행에 있다면, 두 개는 같은 나무판자
두개의 '|'가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자

'''
import sys
input = sys.stdin.readline
R, C = map(int, input().split())
dr = (0, 1)
dc = (1, 0)
def go(x):
    if x == '-': return 1 
    if x == '|': return -1
a = [list(map(go, input().rstrip())) for _ in range(R)]
ans = 0

for i in range(R):
    prev = 0
    for j in range(C):
        if prev == 1 and a[i][j] == 1: continue
        if a[i][j] == 1: 
            ans += 1
            prev = 1
            continue
        prev = -1
for j in range(C):
    prev = 0
    for i in range(R): 
        if prev == -1 and a[i][j] == -1: continue
        if a[i][j] == -1:
            ans += 1
            prev = -1
            continue
        prev = 1
print(ans)