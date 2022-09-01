'''
https://www.acmicpc.net/problem/2644

부모 자식들 간의 관계가 주어졌을 때, 
주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

입력) 사람들은 1, 2 ... n 의 연속적인 번호로 각각 표시된다.
- 1 : 전체 사람수 n [1 \ 100] 
- 2 : 촌수를 계산해야하는 두 사람의 번호
- 3 : 부모 자식들의 간의 관계의 개수 m (양방향)
- 4[m] : 부모 자식 관계를 나타내는 번호 x, y 가 각줄에 나타난다.
        ( 각사람의 부모는 최대 한명만 주저진다 )
출력)
- 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다.
- 촌수계산이 불가능할 때 출력 -1 
'''
from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())
_list = [[] for _ in range(n + 1)]
visited = [False] * (n + 1) 
for _ in range(m):
    x, y = map(int, input().split())
    _list[x].append(y)
    _list[y].append(x)

def bfs(start, end):
    visited[start] = True
    q = deque()
    q.append((start, 0))
    while q:
        r, d = q.popleft() 
        if r == end:
            return d
        nd = d + 1
        for i in _list[r]:
            if not visited[i]:
                q.append((i, nd))
                visited[i] = True
    return -1

print(bfs(start, end))