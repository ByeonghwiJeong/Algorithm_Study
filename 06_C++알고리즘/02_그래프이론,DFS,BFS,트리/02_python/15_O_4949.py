import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.': break
    stk = []
    flag = 1
    for i in s:
        if i == ')':
            if len(stk) == 0 or stk[-1] == '[':
                flag = 0
                break
            else: stk.pop()
        if i == ']':
            if len(stk) == 0 or stk[-1] == '(':
                flag = 0
                break
            else: stk.pop()
        if i == '(': stk.append(i)
        if i == '[': stk.append(i)
    if len(stk) == 0 and flag: print('yes')
    else: print('no')