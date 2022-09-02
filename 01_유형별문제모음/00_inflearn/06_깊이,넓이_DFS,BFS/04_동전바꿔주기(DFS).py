'''
명보네 동네 가게의 현금 출납기에는 k가지 동전이 각각
n1, n2, n3, ...nk 개씩들어있다

T원을 동전으로 바꾸려고한다.
교환하는 방법의 가지수를 계산하시오

입력)
- 1 : 지폐의 금액 T[0 \ 10000]
- 2 : 동전의 가지수
- 3 : 동전의 금액pi & 개수ni
----
20
3
5 3
10 2
1 5
----
출력) 가지 수 출력 - 교환할 수 없는 경우는 존재하지않는다
4
'''
import sys

def dfs(L, sum):
    global cnt
    if sum > m:
        return
    if L == n:
        if sum == m:
            cnt += 1
    else:
        for i in range(cn[L] + 1):
            dfs(L + 1, sum + (cv[L]*i))


m = int(input())
n = int(input())
cv = list()
cn = list()
cnt = 0
dfs(0, 0)
print(cnt)