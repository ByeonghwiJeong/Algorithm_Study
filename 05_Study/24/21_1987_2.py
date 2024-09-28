'''
https://www.acmicpc.net/problem/1987

제목 : 알파벳

문제)
- 세로 R칸, 가로 C칸
- 각 칸에는 대붐낮 알파벳이 하나씩 적혀 있음
- 말은 상하좌우 이동가능
- 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야한다.(같은 알파벳 지나갈수 없음)
- 왼쪽 위에서 출발

입력)
- 1 : R C 가 빈칸을 사이에 두고 주어진다.
- 2 :[R lines] C개의 알파벳

출력)
- 말이 지나갈수 있는 최대 칸수

ex)
2 4
CAAB
ADCB
'''
# TODO : 시간초과 발생 -> Memo해야함
import sys
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c, cnt, bitmask):
    global ret

    ret = max(ret, cnt)
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            next_char = ord(a[nr][nc]) - 65
            if not (bitmask & (1 << next_char)):
                dfs(nr, nc, cnt + 1, bitmask | (1 << next_char))

R, C = map(int, input().split())
a = [input().rstrip() for _ in range(R)]

ret = 0
start_char = ord(a[0][0]) - 65

dfs(0, 0, 1, 1 << start_char)

print(ret)

'''
⭐⭐⭐`비트 마스킹`⭐⭐⭐
공집합에 x를 추가
=> x번째에 1을 or연산자로 추가 
=> n의 범위가 최대 20 (n이 30이하이므로 비트마스킹 적용가능)
### `add` : x번째 비트 ON
- `n |= (1 << x)`
- OR연산자는 이미 있는경우는 무시

### `remove` : x번째 비트 OFF
- `n &= ~(1 << x)`

### `check` : x번째 비트 확인
- `if(n & (1 << x))`
- python 삼항 연산자
    - 참인경우 if 조건 else 거짓인경우

### `toggle` : x번째 비트 XOR연산
- 0은 1, 1은 0
    - x가 있으면 x를 제거, 없으면 x를 추가
- `n ^= (1 << x)`

### `all` : 크기가 21인 집합의 모든 비트를 켜기
- 1 ~ 20 표현하기위해서 크기 21
- `(1 << 21) - 1`

###  `empty` : 공집합으로 만들기
- n = 0
'''
