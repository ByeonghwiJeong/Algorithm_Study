'''
https://www.acmicpc.net/problem/15658
제목 : 연산자 끼워넣기 (2)

문제)
-

입력)

출력)
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_result = float('-inf')
min_result = float('inf')


operations = [ # operators index와 연산 동일
    lambda x, y: x + y,  
    lambda x, y: x - y, 
    lambda x, y: x * y,  
    lambda x, y: x // y if x >= 0 else -(-x // y)  
]

def dfs(idx, result, operators): 
    if idx == N:
        return result, result
    
    max_result = float('-inf')
    min_result = float('inf')
    
    for i, calculator in enumerate(operations):
        if operators[i] > 0:
            operators[i] -= 1
            max_output, min_output = dfs(idx + 1, calculator(result, arr[idx]), operators)
            operators[i] += 1

            max_result = max(max_result, max_output)
            min_result = min(min_result, min_output)

    return max_result, min_result

max_result, min_result = dfs(1, arr[0], operators) 

print(max_result)
print(min_result)