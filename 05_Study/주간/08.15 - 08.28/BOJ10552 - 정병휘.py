'''
문제)
TV채널번호 [1, M]번
각 사람은 선호채널과 비선호채널이 있음

현재 채널이 특정 사람의 비선호 채널이면, 그 사람은 자기 자신의 선호채널로 돌림
그 채널을 싫어하는사람이 두 사람인 경우 어린사람이 자신의 선호체널로 돌림
이과정을 계속해서 진행

입력)
    - 1 : 사람수 N, 채널수 M  [1 ~ 100000], 시작채널 P
    - 2 ~ N+1 : 선호채널 a, 비선호채널 b ~ youngest to oldest
                [1, M] 
출력)
    - 채널 변경수
'''
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, M, P = map(int, input().split())
graph = [[] for _ in range(M+1)] # 2차원 배열 선언 / row index =  비선호채널
visited = [False] * (M + 1) # 채널방문여부
times = 0 # 채널변경 횟수


for _ in range(N):
    a, b = map(int, input().split())
    graph[b].append(a) #비선호 채널index에 선호채널을 push


def dfs(s):
    global times # 전역변수
    visited[s] = True # 방문 체크
    if graph[s]: # 그 채널이 비선호 채널이면
        next = graph[s][0] # 비선호 채널을 가지는 첫번째 사람의 선호채널(가장 어린사람)
        if not visited[next]: # 방문 하지 않은 경우
            times += 1
            dfs(next)
        else: # 방문한경우
            times = -1
            return 


dfs(P)
print(times)