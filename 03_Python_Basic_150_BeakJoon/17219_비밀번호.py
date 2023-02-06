import sys
input = sys.stdin.readline

M, N = map(int, input().split())

passwords = {}
for _ in range(M):
    a, p = input().split()
    passwords[a] = p

for _ in range(N):
    print(passwords[input().strip()])