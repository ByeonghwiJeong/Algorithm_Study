'''
https://www.acmicpc.net/problem/1110
0보다 크거나 같고 99보다 작거나 같은 정수가 주어질 때
다음과 같은 연산을 할 수 있다.

1. 주어진수가 10보다 작다면 앞에 0을 붙여 두자리로 만들고,
    각 자리의 숫자를 더한다.
2. 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 
    합의 가장 오른쪽 자리수를 이어 붙이면 새로운 수를 만들 수 있다.
예) 26 >> 2 + 6 = 8 
     ^            ^  >>> 68
    68 >> 6 + 8 = 14 
     ^             ^ >>> 84 

'''
n = int(input())
ret = 0
temp = n

def go(x):
    if str(x) == 1: x = 10 * x
    s, r = divmod(x, 10)
    return r * 10 + (s + r) % 10

while True:
    temp = go(temp)
    ret += 1
    if temp == n: break
    
print(ret)

