'''
< 동전 뒤집기 >
https://www.acmicpc.net/problem/1285
문제)
- N^2 개의 동전이 N행N열을 이루어 탁자 위에 놓여있다.
- 일부는 앞면(H)이 위를 향하도록 놓여있고, 
- 나머지는 뒷면(T)이 위를 항하도록 놓여있다.
- 임의의 한행이나 한열에 놓인 동전을 모두 뒤집는 작업을 수행
- 뒷면(T)이 위를 향하는 동전 개수를 최소로 하려한다.
- 최소의 개수???
입력)
- 1     : N ~ [1 \ 20]
- 2[N]  : N줄에 걸쳐 N개씩 동전들의초기 상태가 주어진다.
출력)
- 뒷면 최소 갯수
'''
import sys
input = sys.stdin.readline

N = int(input())
a = [0] * 2 * (N + 1)
ret = 987654321

def go(here):
    global ret
    if here == N + 1:
        sum = 0
        i = 1
        while i <= (1 << (N - 1)):
            cnt = 0
            for j in range(1, N + 1):
                if a[j] & i: cnt += 1
            sum += min(cnt, N - cnt)
            i *= 2
        ret = min(ret, sum)
        return
    
    go(here + 1)
    a[here] = ~a[here]
    go(here + 1)

for i in range(1, N + 1):
    s = input().rstrip()
    value = 1
    for j in range(0, len(s)):
        if s[j] == 'T': a[i] |= value
        value *= 2
go(1)
print(ret)


'''
- 2^40 승....???
    - No !!! 2^20 
    - 행을 집으면 열의 최적해는 정해져있다.
- 비트마스킹
    - HHTHH > 숫자로 표현
    - 비트마스킹은 왼쪽부터 오른쪽방향으로 숫자 커지도록!
3
HHT > 4
THH > 1
THT > 1 + 4 > 5
'''