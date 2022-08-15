'''
1 ~ N 중에서 M개의 중복이 없는 수열
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
chk = [False] * (N + 1)
rs = []

def recur(n):
    if n == M:
        print(*rs, sep=' ')
        return 
    for i in range(1, N + 1):
        if chk[i] == False:
            rs.append(i)
            chk[i] = True
            recur(n + 1)
            chk[i] = False
            rs.pop()
recur(0)