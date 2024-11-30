"""
https://www.acmicpc.net/problem/8979
제목: 올림픽

문제)
- 올림픽 순위 규칙
    1. 금메달 수가 더 많은 나라
    2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
    3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라
- 공동 순위가 존재할 수 있음 (3등이 2개인 경우, 4등은 없음)
- 입력받은 국가 K의 등수를 하나의 정수로 출력

입력 예시)
4 3      - 나라 수, 알고 싶은 나라의 등수
1 1 2 0  - 나라번호, 금, 은, 동메달 수
2 0 1 0
3 0 1 0
4 0 0 1
출력 예시)
2
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
rank = [list(map(int, input().split())) for _ in range(N)]
rank.sort(key=lambda x: (-x[1], -x[2], -x[3]))

current_rank = 1
same_rank_count = 1

if rank[0][0] == K:
    print(current_rank)


for i in range(1, N):
    if rank[i][1:] == rank[i - 1][1:]: # 이전 국가와 메달 개수가 동일하면 동일 순위 유지
        same_rank_count += 1
    else:
        # 메달 수가 다르면 현재 순위 갱신
        current_rank += same_rank_count
        same_rank_count = 1  

    if rank[i][0] == K:
        print(current_rank)
        break

