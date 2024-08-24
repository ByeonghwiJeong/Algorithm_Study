'''
https://www.acmicpc.net/problem/23971

제목 : ZOAC 4

문제)
- 한 명씩 앉을 수 있는 테이블이 행마다 W개씩 H행
- 모둔 참가자는 세로로 N칸, 가로로 M칸 이상 비우고 앉아야 함

입력)
- 1 : H, W, N, M ~ [1, 50_000]
    - H : 행의 개수
    - W : 한 행에 앉을 수 있는 사람의 수
    - N : 세로로 N칸
    - M : 가로로 M칸
'''
import sys
import math
input = sys.stdin.readline

H, W, N, M = map(int, input().split())
result = math.ceil(H/(N+1)) * math.ceil(W/(M+1))

print(result)

