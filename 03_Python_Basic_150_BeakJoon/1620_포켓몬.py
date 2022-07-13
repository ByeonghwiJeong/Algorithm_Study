import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokets = dict()
for i in range(1, N+1):
    s = input().strip()
    pokets[s] = i
    pokets[i] = s

for _ in range(M):
    chk = input().strip()
    try:
        print(pokets[int(chk)])

    except:
        print(pokets[chk])