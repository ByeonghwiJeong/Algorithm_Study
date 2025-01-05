'''
https://www.acmicpc.net/problem/14888
제목 : 연산자 끼워넣기

문제)
- N개의 수로 이루어진 수열 A1, A2, ..., AN
- 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자
- 예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, \
    주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. \
    예를 들어, 아래와 같은 식을 만들 수 있다.

1+2+3-4×5÷6
1÷2+3+4-5×6
1+2÷3×4-5+6
1÷2×3-4+5+6

- 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
- 나눗셈은 정수 나눗셈으로 몫만 취한다
- 음수 나누기 양수 경우 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다


입력)
2         - N : 수의 개수 ~ [2, 11]
5 6       - N개의 수 ~ [1, 100]
0 0 1 0   - 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)의 개수

출력) 
30        - 만든식 결과의 최대값
30        - 만든식 결과의 최소값
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_result = float('-inf')
min_result = float('inf')


operations = [
    lambda x, y: x + y,  
    lambda x, y: x - y, 
    lambda x, y: x * y,  
    lambda x, y: x // y if x >= 0 else -(-x // y)  
]

def dfs(idx, result, operators): 
    global max_result, min_result
    if idx == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    for i, calculator in enumerate(operations):
        if operators[i] > 0:
            operators[i] -= 1
            dfs(idx + 1, calculator(result, arr[idx]), operators)
            operators[i] += 1


dfs(1, arr[0], operators) 

print(max_result)
print(min_result)