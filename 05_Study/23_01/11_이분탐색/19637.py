'''
< IF문 좀 대신 써줘 >
문제)
- 전투력 <= 10,000 : WEAK
- 10,000 < 전투력 <= 100,000 : NORMAL
- 100,000 < 전투력 <= 1,000,000 : STRONG
입력)
- 1     : 칭호의 개수 N, 캐릭터들의 개수 M ~ [1 \ 10^5]
- 2[N]  : 칭호, 전투력 상한값
- 3[M]  : 전투력 상한값
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