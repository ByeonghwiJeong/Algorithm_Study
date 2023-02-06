'''
케빈 베이컨의 6단계 법칙에 의하면 지구에 있는 모든 사람들은 6단계이내에서 서로 아는 사람으로 연결
임의의 두 사람이 최소 몇단계만에 이어질 수 있는지 계산하는 게임

[[ 양방향 그래프 문제 ]]
>>>> 인접행렬 or 인접리스트
인접리스트 방식으로 풀이(상관없음)

그래프가 1-base 로 두가지 방법중 하나를 선택해야한다.
1) adj선언시 range(N+1) >>>> 1 base 사용
2) a와 b를 받을 때 각각 -1 >>>> 0 base로 변환

[[ 최단거리문제 >> DFS ]]

유저수 N (2<=N<=100)
친구관계의수 M (1<=M<=5000)
-------
입력)
5 5
1 3
1 4
4 5
4 3
3 2
for row in adj: >> print(row)
0[2, 3]
1[2]
2[0, 3, 1]
3[0, 4, 2]
4[3]
'''
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

kevin = []
ans = (-1, float('inf'))

def bfs(start, goal):
    chk = [False] * N
    chk[start] = True
    dq = deque()
    dq.append((start, 0))
    while dq:
        now, d = dq.popleft()
        if now == goal:
            return  d
        nd = d + 1
        for nxt in adj[now]:
            if not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt, nd))

def get_kevin(start):
    tot = 0
    for i in range(N):
        if i != start:
            tot += bfs(start, i)    
    return tot

for i in range(N):
    kevin.append(get_kevin(i))

for i, v in enumerate(kevin):
    #  같은 경우 처리 : 1 2 3 4 순서대로 진행하므로 같으면 작은숫자에서 변화 X
    #  등호 처리를 통해서 앞뒤 선택가능!!
    if ans[1] > v:
        ans = (i, v)

print(ans[0]+1)
# 처음에 0베이스로 -1을 적용했으므로 +1