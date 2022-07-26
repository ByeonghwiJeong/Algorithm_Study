import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set()
B = set()
for _ in range(N):
    A.add(input().rstrip())
for _ in range(M):
    B.add(input().rstrip())

ans = sorted(list(A & B))
print(len(ans))
print(*ans, sep='\n')