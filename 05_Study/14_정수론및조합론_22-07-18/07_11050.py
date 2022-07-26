'''
nCr = n-1Cr + n-1Cr-1
nCn = 1 nC0 = 1

< chk 선언 >
chk = [[0] * 11 for _ in range(11)]

< 이항계수 함수 선언 > - dynamic programming
1. chk 유무 확인
    - 있으면 chk 반환
2. nCn = 1 nC0 = 1 인경우
    - chk에 1할당
3. chk에 n-1Cr + n-1Cr-1 할당

Last. chk[n][r] 반환
'''
import sys
input = sys.stdin.readline

chk = [[0] * 11 for _ in range(11)]

def bino(n, r):
    if chk[n][r]:
        return chk[n][r]
    if r == n or r == 0:
        chk[n][r] = 1
    else:
        chk[n][r] = bino(n-1, r) + bino(n-1, r-1)
    return chk[n][r]
N, K = map(int, input().split())
print(bino(N, K))
