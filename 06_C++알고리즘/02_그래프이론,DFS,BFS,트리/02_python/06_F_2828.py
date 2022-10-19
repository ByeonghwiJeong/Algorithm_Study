import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())
l = 1
ret = 0
for i in range(j):
    r = l + m -1
    temp = int(input())
    if l <= temp <= r: continue
    elif temp < l:
        ret += l - temp
        l = temp
    elif temp > r:
        ret += temp - r;
        l += temp - r;
print(ret)
    