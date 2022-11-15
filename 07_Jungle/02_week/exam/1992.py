import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().rstrip())) for _ in range(n)]
ret = ''

def check(sr, sc, l):
    temp = a[sr][sc]
    for i in range(sr, sr + l):
        for j in range(sc, sc + l):
            if a[i][j] != temp: return False
    return True

def recur(r, c, l):
    global ret
    if check(r, c, l):
        temp = a[r][c]
        if temp == 1: ret += '1'
        if temp == 0: ret += '0'
        return
    else:
        l //= 2
        mr = r + l
        mc = c + l
        ret += '('
        recur(r, c, l)
        recur(r, mc, l)
        recur(mr, c, l)
        recur(mr, mc, l)
        ret += ')'

recur(0, 0, n)
print(ret)