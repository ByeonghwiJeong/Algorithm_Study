'''
< N-Queen >
https://www.acmicpc.net/problem/9663

N x N 체스판 

pos_diag ~ 합일정 : set에 추가
neg_diag ~ 차일정 : set에 추가



'''
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
result = 0
row = set()
pos_diag = set()
neg_diag = set()
dp = [0] * n

def dfs(x):
    global row, pos_diag, neg_diag, result
    if x == n:
        result += 1
        return
    for i in range(n):
        if i in row:
            continue
        if i-x in pos_diag:
            continue
        if i+x in neg_diag:
            continue
        dp[x] = i
        row.add(i)
        pos_diag.add(i-x)
        neg_diag.add(i+x)
        dfs(x + 1)
        row.remove(i)
        pos_diag.remove(i-x)
        neg_diag.remove(i+x)


dfs(0)
print(result)