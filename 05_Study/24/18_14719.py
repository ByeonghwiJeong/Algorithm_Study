'''
https://www.acmicpc.net/problem/14719
제목 : 빗물

문제)
- 2차원 세계에 블록이 쌓여있음
- 비는 충분이 올때 고이는 빗물의 총량

입력)
- 1 : H, W ~ [1, 500]
- 2 : 0이상 H이하의 정수가 2차원 세계 맨 왼쪽부터 맨 오른쪽까지 W개 주어짐

출력)
- 빗물의 총량
'''
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0

# 양끝 제외하고 그 위치 기준 양쪽 높이 check
# 그 높이해서 내 높이 비교후 차감
for i in range(1, W-1):
    l = max(blocks[:i])
    r = max(blocks[i+1:]) 
    min_h = min(l, r) 
    if min_h > blocks[i]: 
        answer += min_h - blocks[i]

print(answer)