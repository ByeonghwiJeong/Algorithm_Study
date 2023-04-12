"""
< 전깃줄 >
https://www.acmicpc.net/problem/2565
문제)
- 두 전봇대 A, B 사이에 전깃줄 설치
- 서로 교차하는 경우 발생
- 전깃줄이 연결위치는 위에서 부터 차례대로 번호가 매겨져 있음
- 남아있는 모든 전깃줄이 서로 교차하지 않도록 하려고 함
- 최소 전깃줄 개수를 구하라
"""
from bisect import bisect_left
import sys

input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort(key=lambda x: x[0])
stack = [0]
for i, j in lines:
    if stack[-1] < j:
        stack.append(j)
    else:
        # for k in range(len(stack)):
        #     if stack[k] >= j:
        #         stack[k] = j
        #         break
        stack[bisect_left(stack, j)] = j
print(N - len(stack) + 1)

"""
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
---
1 8
2 2
3 9
4 1
6 4
7 6
9 7
10 10
왼쪽과 오른쪽이 증가해야 교차하지않음
sort 이후에 두번째에서 가장 긴 증가하는 수열 (LIS)
2 4 6 7 10
1 4 6 7 10
"""
