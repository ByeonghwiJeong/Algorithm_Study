"""
https://www.acmicpc.net/problem/2828
문제 : 사과 담기 게임
- 바구니를 옮기는 오래된 게임을 한다.
- 스크린은 N칸
- 스크린아래쪽에는 M칸의 바구니가 있다.
- (M < N)
- 바구니는 좌우로 움직일 수 있다.
- 가장 처음에 바구니는 왼쪽 M칸을 차지
- 사과를 모두 담으려고 한다. 이때
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = 1 # 왼쪽
r = l + M - 1 # 오른쪽
dis = 0
for _ in range(int(input())):
    temp = int(input())
    if temp < l: # 왼쪽으로 이동
        dis += l - temp
        l = temp 
        r = l + M - 1
    elif temp > r: # 오른쪽으로 이동
        dis += temp - r;
        r = temp
        l = r - M + 1
print(dis)
    