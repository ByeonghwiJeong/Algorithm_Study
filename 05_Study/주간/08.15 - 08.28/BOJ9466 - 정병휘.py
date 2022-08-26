'''
<단방향 그래프>

입력) 테스트 케이스
    - 학생수 정수 n 으로 주어진다.
    - 각 테스트 케이스 둘째줄에는 선택 된 학생들의 번호가 부여
        [1 \ n]
출력) 팀에 속하지 못한 학생 수
'''
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 수

def dfs(x):
    global visited, one_loop, team
    visited[x] = True # 전체 방문처리
    checkset.add(x) 
    team.append(x) 
    next = graph[x]
    if not visited[next]: # 전체 loop에서 방문 X
        return dfs(next)
    else: # 전체 loop 방문 O
        if next in checkset:
            idx = team.index(next)
            team = team[idx:]
            return team
        return []


for _ in range(T):
    n = int(input()) # 학생 수
    graph = [0] + list(map(int, input().split())) # 선호학생 1차원 배열
    visited = [False] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            checkset = set()
            team = []
            result += dfs(i)
    print(n - len(result))



