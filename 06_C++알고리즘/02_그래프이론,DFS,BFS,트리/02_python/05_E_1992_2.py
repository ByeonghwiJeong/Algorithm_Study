import sys
input = sys.stdin.readline

def chk(r1, c1, r2, c2):
    temp = a[r1][c1]
    for i in range(r1, r2):
        for j in range(c1, c2):
            if(temp != a[i][j]):
                return False
    return True

def recur(r1, c1, r2, c2):
    if chk(r1, c1, r2, c2):
        return a[r1][c1]
    mr = (r1 + r2) // 2
    mc = (c1 + c2) // 2
    ans = ""
    ans += "("
    ans += recur(r1, c1, mr, mc)
    ans += recur(r1, mc, mr, c2)
    ans += recur(mr, c1, r2, mc)
    ans += recur(mr, mc, r2, c2)
    ans += ")"
    return ans

n = int(input())
a = [input().rstrip() for _ in range(n)]
print(recur(0, 0, n, n))