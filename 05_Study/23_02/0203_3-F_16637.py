'''
< 괄호 추가하기 >
https://www.acmicpc.net/problem/16637
문제)
- 길이가 N인 수식 
- 0 ~ 9정수와 연산자(+, -, x)로 이루어져 있다.
- 수식계산시 왼쪽부터 순서대로 계산 (연산자 우선 순위 동일)
- 괄호를 추가하면 우선순위
- 충첩괄호 사용X
- 수식이 주어졌을 때, 괄호를 적절히 추가해서 최댓값을 구하시오
- 괄호 개수의 제한은 없으며, 추가하지 않아도 된다.
입력)
- 
'''
import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
number = []
operation = []
ret = -987654321

def oper(a, b, c):
    if a == "+": return b + c;
    if a == "-": return b - c;
    if a == "*": return b * c;

def go(idx, s):
    global ret
    if idx == len(number) - 1:
        ret = max(ret, s)
        return
    # 기본순서
    go(idx + 1, oper(operation[idx], s, number[idx+1]))
    # 뒤에 괄호가 있을때 
    if idx + 2 <= len(number) - 1:
        t = oper(operation[idx + 1], number[idx + 1], number[idx + 2])
        go(idx + 2, oper(operation[idx], s, t)) # 
    return

for i in range(N):
    if i % 2: operation.append(S[i])
    else: number.append(int(S[i]))

go(0, number[0])
print(ret)

'''
중요 포인트 
- 누적합과 현재 index를 기반
- 뒤에 괄호가 있을때 index처리 조건 주의!!!
- operation과 number를 다른 배열로 분리
'''
