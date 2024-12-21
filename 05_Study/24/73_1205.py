"""
https://www.acmicpc.net/problem/1205
제목: 등수 구하기

문제)
- 랭킹 리스트 : 매번 게임할 때 마다 얻는 점수가 비오름차순으로 저장
- 랭킹 리스트가 100, 90, 90, 80일 때 각각의 등수는 1, 2, 2, 4등
- 랭킹 리스트에 올라 갈 수 있는 점수의 개수 P
- 리스트에 있는 점수 N개가 비오름차순
- 태수의 새로운 점수
- 태수의 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하는 프로그램을 작성
- 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1을 출력
- 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다

입력)
- N, 태수의 새로운 점수, P
- 현재 랭킹 리스트에 있는 점수가 비오름차순

입력예시)
10 1 10
10 9 8 7 6 5 4 3 2 1
출력예시)
-1
"""

import sys
input = sys.stdin.readline

N, new_score, P = map(int, input().split())
scores = list(map(int, input().split()))

if N == 0:
    print(1)
else:
    if N == P and scores[-1] >= new_score:
        print(-1)
    else:
        rank = 1
        for i in range(N):
            if scores[i] > new_score:
                rank += 1
        print(rank)