"""
https://www.acmicpc.net/problem/1315
백준 1315. RPG, P3
- 게임에서 캐릭터는 2가지 스탯 (STR, INT)를 가짐
- 캐릭터 생성시 두 스탯은 모두 1
- N개의 퀘스트가 있음
- i번째 퀘스트를 수행 조건
    - 캐릭터 힘 >= STR[i] OR 캐릭터 지력 >= INT[i]
    - 퀘스트 수행시 PNT[i]만큼의 포인트 획득
- 퀘스트 수행 순서는 자유롭게
- 포인트로 원하는 스탯을 강화 가능
- 퀘스트 개수의 최댓값
입력)
- 퀘스트의 수 :  N ~ [1, 50]
- N줄 ~ STR[i], INT[i], PNT[i] 
    - STR, INT, PNT ~ [1, 1000]
---------------------------------
->> DP[STR][INT] : STR, INT일 때 퀘스트의 최대 개수
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
quests = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(1001)] for _ in range(1001)]
visited = [0 for _ in range(N + 1)]

def rpg(str, int):
    if dp[str][int] != -1: return dp[str][int]
    dp[str][int] = 0
    pnt = 0
    pos_check = []
    for i in range(N):
        if str >= quests[i][0] or int >= quests[i][1]: # 퀘스트 수행 가능한 경우
            dp[str][int] += 1
            if not visited[i]:  # 방문하지 않은 퀘스트인 경우
                visited[i] = 1
                pnt += quests[i][2]
                pos_check.append(i)

    for p in range(0, pnt + 1):
        next_str = min(1000, str + p)
        next_int = min(1000, int + pnt - p)
        dp[str][int] = max(dp[str][int], rpg(next_str, next_int))

    for i in pos_check:
        visited[i] = 0
        
    return dp[str][int]

print(rpg(1, 1))



