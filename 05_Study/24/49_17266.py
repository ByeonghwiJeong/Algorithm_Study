"""
https://www.acmicpc.net/problem/17266
제목: 어두운 굴다리

문제)
- 굴다리의 길이 N  ~ [1, 100_000]
- M개의 가로등이 있음 ~ [1, N]
- 설치할 수 있는 가로등의 위치 x가 주어짐 ~ [0, N]
    (오름 차순으로 입력 받으며 가로등의 위치는 중복되지 않음)
- 길이 N을 밝히기 위한 가로등의 최소 높이를 구하라
- H높이의 가로등은 좌우로 H만큼의 거리를 밝힘

입력 예시)
5
2
2 4
출력 예시)
2
"""

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
light_positions = list(map(int, input().split()))


def is_possible_height(height):
    if light_positions[0] - height > 0:  # 첫번째 가로등 왼쪽 체크
        return False
    if N - light_positions[-1] > height: # 마지막 가로등 오른쪽 체크
        return False
    for i in range(1, M): # 나머지 가로등 간격 체크
        if light_positions[i] - light_positions[i-1] > 2 * height:
            return False
    return True


def binary_search():
    left = 0
    right = N
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if is_possible_height(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

print(binary_search())