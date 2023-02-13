'''
< 집합 >
https://www.acmicpc.net/problem/11723
문제)
- 비어 있는 공집합S가 주어짐, 아래 연산을 수행
- x ~ [1, 20]
    - "add x": S에 x를 추가
        - x가 이미 있는경우 연산 무시
    - "remove x": S에 x를 제거
        - x가 없는경우 연산 무시
    - "check x": S에 x가 있으면 1을, 없으면 0을 출력
    - "toggle x": S에 x가 있으면 x를 제거, 없으면 x를 추가
    - "all": S를 1, 2, ..., 20으로 바꾼다.
    - "empty": S를 공집합
입력)
- 1     : 연산의 수 M ~ [1 \ 3,000,000]
- 2[M]  : 연산
    - 양방향
출력)
- 1     : check 연산주어질때 마다 결과를 출력
'''
import sys
input = sys.stdin.readline

x = 0
n = 0

for _ in range(int(input())):
    a = input().split()
    if a[0] == "add": n |= (1 << int(a[1]))
    elif a[0] == "remove": n &= ~(1 << int(a[1]))
    elif a[0] == "check": print(1 if n&(1 << int(a[1])) else 0)
    elif a[0] == "toggle": n ^= (1 << int(a[1]))
    elif a[0] == "all": n = (1 << 21) - 1
    elif a[0] == "empty": n = 0

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
