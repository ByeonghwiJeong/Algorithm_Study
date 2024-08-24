'''
https://www.acmicpc.net/problem/19637

제목 : IF문 좀 대신 써줘

문제)
- 
'''


from bisect import bisect_left
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [] # 칭호
B = [] # 전투력
# 칭호 & 전투력
for _ in range(N):
    a, b = input().split()
    A.append(a)
    B.append(int(b))

for _ in range(M):
    print(A[bisect_left(B, int(input()))])