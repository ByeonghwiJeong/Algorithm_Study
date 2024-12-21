"""
https://www.acmicpc.net/problem/22866
제목: 탑 보기

문제)
- 일직선으로 다양한 높이의 건물이 총 N개가 존재
- 번호 순서대로 건물
- 현재 있는 건물의 높이가 L이라고 하면 L만큼 높이가 있는 건물이 보이게 된다.
- 바라보는 방향으로 높이가 L인 건물 뒤에 L이하 건물이 있으면 보이지 않는다.

입력)
- 첫째 줄에 건물의 개수 N이 주어진다. (1 <= N <= 100)
- 둘째 줄에 건물의 높이가 주어진다. (1 <= 높이 <= 100)

출력)
- i번째 건물에서 보이는 건물의 개수
- 만약 한개 이상이면 가장 가까운 건물의 번호를 출력

입력 예시)
8
3 7 1 6 3 5 1 7
출력 예시)
1 2
0
3 2
2 2
4 4
3 4
4 6
0
"""

import sys
input = sys.stdin.readline
INF = 10**9

N = int(input())
heights = list(map(int, input().split()))

# 결과를 저장할 리스트
ans_cnt = [0] * N
ans_min_num = [INF] * N

# i번 건물의 좌측 관찰
stack = []
for i in range(N):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()  # 가려지는 건물 제거
    
    if stack:  # 스택에 남아있는 가장 가까운 건물
        ans_cnt[i] += len(stack)  # 보이는 건물 개수
        ans_min_num[i] = stack[-1] + 1  # 건물 번호 (1-indexed)
    
    stack.append(i)  # 현재 건물을 스택에 추가

# i번 건물의 우측 관찰
stack = []
for i in range(N-1, -1, -1):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()  # 가려지는 건물 제거
    
    if stack:  # 스택에 남아있는 가장 가까운 건물
        ans_cnt[i] += len(stack)  # 보이는 건물 개수
        # 가까운 건물 번호가 이전 값보다 작은 경우만 갱신
        if ans_cnt[i] == 1 or (stack[-1] + 1 < ans_min_num[i]):
            ans_min_num[i] = stack[-1] + 1  # 건물 번호 (1-indexed)
    
    stack.append(i)  # 현재 건물을 스택에 추가

# 최종 출력
for i in range(N):
    if ans_cnt[i] == 0:
        print("0")
    else:
        print(f"{ans_cnt[i]} {ans_min_num[i]}")