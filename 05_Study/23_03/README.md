## ✏️0320. [5719](https://www.acmicpc.net/problem/5719)

### ⭐⭐⭐`비트 마스킹`⭐⭐⭐

공집합에 x를 추가
=> x번째에 1을 or연산자로 추가
=> n의 범위가 최대 20 (n이 30이하이므로 비트마스킹 적용가능)

<img width="600" alt="image" src="https://user-images.githubusercontent.com/95831345/227275512-ee68412c-cda2-4499-b4b2-3779b6b99213.png">

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

### `empty` : 공집합으로 만들기

- n = 0

## ✏️0320. [11723](https://www.acmicpc.net/problem/11723)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)

## ✏️. [](https://www.acmicpc.net/problem/)
