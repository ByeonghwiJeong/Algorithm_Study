'''
https://www.acmicpc.net/problem/14391
제목: 종이 조각

문제
- 숫자가 적힌 세로 N줄, 가로 M줄의 종이 조각
- 각 숫자는 0~9
- 세로나 가로의 크기가 1인 직사각형 모양으로 잘라서 숫자를 만든다.
- 가로 조각은 왼쪽부터 오른쪽까지, 세로 조각은 위부터 아래까지
- 종이를 적절히 잘라서 조각의 합을 최대로 하는 프로그램을 작성하라.
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
paper = [list(map(int, list(input().rstrip()))) for _ in range(N)]
ans = 0

# 비트마스킹을 이용한 완전탐색
# 1 << (N*M) : 2^(N*M)가지 경우의 수
# 각 칸을 가로(0) or 세로(1)로 자르는 모든 경우의 수를 표현
for i in range(1 << (N*M)):
    sum = 0
    # 가로 합
    for r in range(N):
        cur = 0
        for c in range(M):
            # 비트 인덱스 계산
            k = r * M + c
            if i & (1 << k) == 0: # 가로로 자르는 경우 (비트가 0인 경우)
                cur = cur * 10 + paper[r][c] # 숫자를 이어붙임
            else: 
                # 세로로 자르는 지점 (가로로 자르는 경우의 합을 더함)
                sum += cur 
                cur = 0
        # 행의 마지막 숫자를 더함
        sum += cur
    # 세로 합
    for c in range(M):
        cur = 0
        for r in range(N):
            k = r * M + c # 비트 인덱스 계산
            if i & (1 << k) != 0: # 세로로 자르는 경우 (비트가 1인 경우)
                cur = cur * 10 + paper[r][c] # 숫자를 이어붙임
            else:
                # 가로로 자르는 지점 (세로로 자르는 경우의 합을 더함)
                sum += cur
                cur = 0
        # 열의 마지막 숫자를 더함
        sum += cur
    ans = max(ans, sum)

print(ans)