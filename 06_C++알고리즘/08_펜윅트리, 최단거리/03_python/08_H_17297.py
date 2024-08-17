'''
https://www.acmicpc.net/problem/17297

제목 : Messi Gimossi
문제)

messi(1): Messi
messi(2)​​: Messi Gimossi
messi(3)​​​​​​: Messi Gimossi Messi
messi(4): Messi Gimossi Messi Messi Gimossi
messi(5): Messi Gimossi Messi Messi Gimossi Messi Gimossi Messi

messi(n) = messi(n-1) + " " + messi(n-2)

messi(N)의 M번째 글자
N이 충분히 크다면 M번째 글자는 무엇인가?

M번째 글자가 공백(' ')이면 "Messi Messi Gimossi"출력
그렇지 않으면 M번째 글자 출력
'''
import sys
input = sys.stdin.readline

M = int(input()) - 1 # index 0부터 시작
S = "Messi Gimossi"
dp = [0, 5, 13] # messi(0), messi(1), messi(2)의 길이

# M이 속한 messi(n) 찾기
while dp[-1] < M:
    dp.append(dp[-1] + dp[-2] + 1)

n = len(dp) - 1 # messi(n)의 n 값

# M의 위치 찾기 (n부터 2까지 역순)
for i in range(n, 1, -1):
    if M >= dp[i]:
        M -= dp[i] + 1
'''
M = 21 이라면 
M -= 1 # M = 20
dp = [0, 5, 13, 19, 33] 
>> range(4, 1, -1)
 - i=4) dp[4] = 33 > 21 : 작업X
 - i=3) dp[3] = 19 < 21 
    : M = 20 - (19 + 1) = 1
 - i=2) dp[2] = 13 > 1 : 작업X

21번째 글자 (index 20)
messi(4) = messi(3) + " " + messi(2)
에서 messi(2)의 1번째 글자를 의미

'''

if M in {5, -1}: print("Messi Messi Gimossi")
else: print(S[M])


