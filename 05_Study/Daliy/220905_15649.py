'''
https://www.acmicpc.net/problem/15649
 
입력)
- 자연수 N, M
출력)
- 1 ~ N 까지 자연수 중에서 중복 없이 M개를 고른 수열

'''
import sys
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
visited = [False] * (N + 1)
rs = []

def recur(x):
    if x == M:
        print(*rs, sep=' ')
        return
    for i in range(1, N + 1):
        if not visited[i]:
            rs.append(i)
            visited[i] = True
            recur(x + 1)
            rs.pop()
            visited[i] = False


recur(0)