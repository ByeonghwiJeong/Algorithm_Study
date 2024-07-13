'''
https://www.acmicpc.net/problem/11723
제목: 집합

'''
import sys

input = sys.stdin.readline



# 비트 연산을 위한 상수
ALL_BITS = (1 << 21) - 1
MAX_NUM = 20

def add(x, num):
    return x | (1 << num)

def remove(x, num):
    return x & ~(1 << num)

def check(x, num):
    return 1 if x & (1 << num) else 0

def toggle(x, num):
    return x ^ (1 << num)

def all_bits():
    return ALL_BITS

def empty():
    return 0

# 명령어 딕셔너리
commands = {
    'add': add,
    'remove': remove,
    'check': check,
    'toggle': toggle,
    'all': lambda x, _: all_bits(),
    'empty': lambda x, _: empty()
}

n = 0
for _ in range(int(input())):
    cmd, *args = input().split()
    if cmd == 'check':
        print(commands[cmd](n, int(args[0]) if args else 0))
    else:
        n = commands[cmd](n, int(args[0]) if args else 0)



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