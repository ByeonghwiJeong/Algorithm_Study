import sys
input = sys.stdin.readline

def quard(r, c, size):
    b = a[r][c]
    if(size == 1): return b  
    half_size = size // 2
    ret = ""
    for i in range(r, r + size):
        for j in range(c, c + size):
            if(b != a[i][j]):
                ret += "("
                ret += quard(r, c, half_size)
                ret += quard(r, c + half_size, half_size)
                ret += quard(r + half_size, c, half_size)
                ret += quard(r + half_size, c + half_size, half_size)
                ret += ")"
                return ret
    return b

n = int(input())
a = [input().rstrip() for _ in range(n)]
print(quard(0, 0, n))