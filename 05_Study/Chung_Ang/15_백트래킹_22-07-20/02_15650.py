'''
15649 15650 15651
3개중에서 50번 문제는 접근 방식이 다름
중요!!!중요!!!중요!!!중요!!!
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
rs = []

def recur(n):
    if len(rs) == M:
        print(*rs, sep=' ')
        return 
    for i in range(n, N + 1):
        if i not in rs:
            rs.append(i)
            recur(i)
            rs.pop()
recur(1)