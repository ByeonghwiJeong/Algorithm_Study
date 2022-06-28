'''
크기가 N x N 도시가 있다. 도시는 1 x 1 크기의 칸으로 나누어져있다.
도시의 각 칸은 (0)빈칸  (1)치킨집  (2)집  중 하나이다.
도시의 칸은 (r, c) r행 c열 또는 위에서 r번째칸  c번째칸을 의미한다.
r와 c는 1부터 시작한다.

치킨거리 : 집 ~ 치킨집  ( 가로 + 세로 )
가장 수익 좋은 치킨집의 개수 : 최대 M개
도시에 있는 치킨집 중에서 최대 M개를 고르고 나머지는 폐업
어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램

도시의 치킨거리 : 모든집의 치킨거리의 합

입력)
    첫째줄 N(2=<N=<50) M(1=<M=<13)
    둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.


13 C 6 = 13 C 7 = 1716
>> 13 C 7 일때 7가지라서 최대 경우

집은 최대 100

100 * 7 * 1716 = 1,201,200


[[ 완전 탐색 가능 ]]
'''
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
store = []
home = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        if city[i][j] == 2:
            store.append((i, j))

ans = float('inf')
for ss in combinations(store, M):
    tot = 0
    for h in home:
        # mindis = float('inf')
        # for s in ss:
        #     mindis = min(mindis, abs(s[0]-h[0])+abs(s[1]-h[1]))
        # tot += mindis
        tot += min(abs(s[0]-h[0])+abs(s[1]-h[1]) for s in ss)

    ans = min(ans, tot)
print(ans)
        
