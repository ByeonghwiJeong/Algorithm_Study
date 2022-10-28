from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
a = list(range(n))
result = 987654321
for s in permutations(a):
    tmp = 0
    flag = 0
    for i in range(len(s) - 1):
        b = l[s[i]][s[i+1]]
        if not b:
            flag = 1 
            continue
        tmp += b
    if flag: continue
    b = l[s[-1]][s[0]]
    if not b: continue
    tmp += b
    if tmp < result:
        result = tmp
print(result)