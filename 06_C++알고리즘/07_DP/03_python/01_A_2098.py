"""
https://www.acmicpc.net/problem/2098
백준 2098. 외판원 순회, G1
- TSP(Traveling Salesman Problem) 문제
- 도시 N ~ [2, 16]
- N 개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 최소 비용
- 도시 i -> 도시 j 로 가는 비용이 W[i][j]로 주어짐
- 비용은 대칭적이지 않을 수 있음
- W[i][i] = 0 : i에서 j로 갈 수 없는 경우
- 한 번 갔던 도시로 다시 갈 수 없음
- 만약에 순서가 상관 있다고 하면 16!
- 출발 도시는 어디든 상관 없음
    - 아래 두 가지 경로의 비용은 같음
    : 2 -> 1 -> 3 -> 4 -> 2
    : 3 -> 4 -> 2 -> 2 -> 1 
    - 1번 도시에서 출발하는 경우로 가정 : OK
- 비트 마스킹 사용 
    - 16 x 16 행렬을 만들어서 visited 저장 대신에 사용
    1. 방문한 도시 추가하기  체크
        - 1(2) | 100(2) == 101(2)
        - visited | (1 << next) # next 현재 방문할 도시
    2. 방문한 도시 확인하기
        - 101(2) & 100(2) == 100(2)
        - visited & (1 << next) # next 현재 방문할 도시
    3. 방문한 도시 삭제하기
        - 101(2) & ~100(2) == 1(2)
        - visited & ~(1 << next) # next 현재 방문할 도시
    4. 모든 도시를 방문했는지 확인하기
        - 101(2) == 111(2)
            - 111(2)는 2^3 - 1 = 7
        - visited == (1 << N) - 1
"""
import sys
input = sys.stdin.readline
INF = 987654321

N = int(input().strip())
dist = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[-1 for _ in range(1 << N)] for _ in range(N)]

def tsp(here, visited):
    if visited == (1 << N) - 1: # 모든 도시를 방문했을 때
        return dist[here][0] if dist[here][0] else INF
    if dp[here][visited] != -1: # 이미 계산한 경우
        return dp[here][visited]
    dp[here][visited] = INF # 초기화
    for i in range(N): # 모든 도시에 대해
        if visited & (1 << i): # 이미 방문한 도시라면
            continue
        if dist[here][i] == 0: # 갈 수 없는 경우
            continue
        dp[here][visited] = min(dp[here][visited], tsp(i, visited | (1 << i)) + dist[here][i]) 
        # 최소값 갱신 
        # tsp(i, visited | (1 << i)) + dist[here][i] : i 도시를 방문한 경우의 최소값 + i 도시로 가는 비용
    return dp[here][visited]

print(tsp(0, 1))