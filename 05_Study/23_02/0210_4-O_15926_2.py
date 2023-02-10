'''
< 현욱은 괄호왕이야! >
https://www.acmicpc.net/problem/15926
문제)
- 괄호 문자열중 가장긴 부분의 문자열의 길이를 계산
입력)
- 1     : n ~ [1 \ 200,000]
- 2     : 괄호문자열
'''
n = int(input())
s = input().rstrip()
stk = [-1]
ret = 0
for i in range(n):
    if s[i] == '(': stk.append(i)
    if s[i] == ')': 
        stk.pop()
        if stk:
            ret = max(ret, i - stk[-1])
        else:
            stk.append(i)
print(ret)

'''
1. stk에 [-1]로 선언
2. for문 i ~ [1 \ n-1]
    1. s[i]가 '('이면 stk에 i push
    2. s[i]가 ')'이면
        - stk.pop() 원소 빼기
        - 스택에 원소 있으면
            - ret = max(ret, i - stk[-1])
        - 스택에 원소 없으면
            - stk.append(i)
'''