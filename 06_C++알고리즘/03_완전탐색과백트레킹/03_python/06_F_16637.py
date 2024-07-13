'''
https://www.acmicpc.net/problem/16637
제목: 괄호 추가하기

- 길이가 N인 수식
- 수식은 왼쪽부터 오른쪽으로 계산
- 괄호 안에는 연산자 하나만 들어가야 함, 먼저 계산
- 중첩 괄호 사용 불가
- 괄호를 적절히 추가해 얻을 수 있는 결과의 최댓값
'''
import sys
from itertools import combinations
input = sys.stdin.readline

def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    
N = int(input())
S = input().strip()
nums = []
ops = []
for i in range(N):
    if i % 2 == 0:
        nums.append(int(S[i]))
    else:
        ops.append(S[i])

result = -987654321

def go(idx, s): # nums index, operation result
    global result
    if idx == len(nums) - 1:
        result = max(result, s)
        return
    
    # 괄호 없이 계산
    go(idx + 1, calc(s, nums[idx + 1], ops[idx]))
    
    # 다음 두 숫자에 괄호 추가
    if idx + 2 < len(nums):
        tmp = calc(nums[idx + 1], nums[idx + 2], ops[idx + 1])
        go(idx + 2, calc(s, tmp, ops[idx]))

go(0, nums[0])
print(result)