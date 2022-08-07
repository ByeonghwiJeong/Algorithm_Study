# queen[n] == queen[i]
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(n):
    if n == N:
        global cnt 
        cnt += 1
        return

    for i in range(N):

        row[n] = i
                
        if is_valid(n):

            dfs(n + 1)

def is_valid(n):
    for i in range(n):
        # 
        if row[n] == row[i] or abs(row[n] - row[i]) == abs(n - i):
            return False
    return True


N = int(input())
cnt = 0
row = [0] * N


dfs(0)
print(cnt)