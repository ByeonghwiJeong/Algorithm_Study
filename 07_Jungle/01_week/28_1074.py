import sys
input = sys.stdin.readline
N, R, C = map(int, input().split())

def recur(r, c, n):
    global result
    if r == R and c == C:
        print(result)
        sys.exit(0)
    if n == 0:
        result += 1
        return
    er = r + 2**n
    ec = c + 2**n
    if not (r <= R < er and c <= C < ec):
        result += (2**(2*n))
        return
    mr = r + 2**(n-1)
    mc = c + 2**(n-1)
    recur(r, c, n - 1)
    recur(r, mc, n - 1)
    recur(mr, c, n - 1)
    recur(mr, mc, n - 1)      

result = 0
recur(0, 0, N) # 2**3