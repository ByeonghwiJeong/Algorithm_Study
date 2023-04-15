"""
< 주사위 윷놀이 >
https://www.acmicpc.net/problem/17825
문제)

"""
import sys
from collections import deque

input = sys.stdin.readline

INF = 987654321
# 주사위 10번 던지기 -> 10개의 숫자
dice = list(map(int, input().split()))
# 말 4개
_pos = [0] * 4
# ========== 지도생성 ==========
graph = [[] for _ in range(33)]
# index 로 연결
for i in range(21):
    graph[i].append(i + 1)
# 왼
graph[5].append(22);graph[22].append(23);graph[23].append(24);graph[24].append(30)
# 아래
graph[10].append(25);graph[25].append(26);graph[26].append(30)
# 오른
graph[15].append(27);graph[27].append(28);graph[28].append(29);graph[29].append(30)
# 위
graph[30].append(31);graph[31].append(32);graph[32].append(20)
# 점수
scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35]
# ======== 지도 완료 ===========

def move(here, cnt):
    if here == 100:
        return 100
    if len(graph[here]) >= 2: # 경로 2개인경우
        here = graph[here][1]
        cnt -= 1
    if cnt:
        q = deque()
        q.append(here)
        while q:
            x = q.popleft()
            nxt = graph[x][0]
            if nxt == 31:
                break
            q.append(nxt)
            cnt -= 1
            if cnt == 0:
                break
        return nxt
    else:
        return here



def go(here):
    if here == 10: # 주사위 10번 던지기 끝
        return 0
    ret = 0
    for i in range(4):
        tmp_idx = _pos[i]
        token_idx = 
