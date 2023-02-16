'''
< Messi Gimossi >
https://www.acmicpc.net/problem/17297
문제)
messi(1): Messi
messi(2)​​: Messi Gimossi
messi(3)​​​​​​: Messi Gimossi Messi
messi(4): Messi Gimossi Messi Messi Gimossi
messi(5): Messi Gimossi Messi Messi Gimossi Messi Gimossi Messi

N이 충분히 클때 M번째 글자?

입력)
- 1     : 정수 M ~ [1 \ 2^30-1]
출력)
- 1     : ' '이 아닐경우 그 알파벳출력 ' '인경우 "Messi Messi Gimossi"출력

'''
import sys
input = sys.stdin.readline

M = int(input())
M -= 1 # index기준이라서 -1
S = "Messi Gimossi"
dp = [0, 5, 13]
while dp[-1] < M:
    dp.append(dp[-2] + 1 + dp[-1])

n = len(dp) - 1
while M >= 13:
    if M >= dp[n]: M -= (dp[n] + 1)
    n -= 1
    
if M == 5 or M == -1: print("Messi Messi Gimossi")
else: print(S[M])

    

'''
1   5
3   517
5   51715
8   517151517
13  517151517151715

0
1
1
2
3
5
8
11
19

'''