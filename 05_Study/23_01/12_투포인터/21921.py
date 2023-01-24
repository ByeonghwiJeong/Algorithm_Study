'''
< 블로그 >
https://www.acmicpc.net/problem/21921
문제)
- 블로그 방문자에 대해서 \
    X일동안 가장 많이 들어온 방문자수와 그 기간들을 알고 싶다.
- X일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구해라!
입력)
- 1     : 블로그 운영 일수 N, 기간 X일
- 2     : 1 ~ N일차까지 하루 방문자 수
출력)
- 1     : X일 동안 가장 많이 들어온 방문자 수 \
        - 최대 방문자수 0이면 "SAD" 출력
- 2     : 0이 아닌경우 기간이 몇개 있는지 출력
'''
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

visiters = 0
# index 0 ~ x-1 방문자수
for i in range(x): visiters += a[i]

ans = visiters # 최대 방문자수
cnt = 1 # 최대 방문자 수의 기간수

for i in range(x, n): # x ~ n-1
    visiters -= a[i - x]
    visiters += a[i]
    if visiters > ans: # 최대 갱신 & 기간수 초기화
        ans = visiters
        cnt = 1
    elif visiters == ans: cnt += 1 # 기간수 +1

if ans: print(ans, cnt, sep='\n')
else: print("SAD")
