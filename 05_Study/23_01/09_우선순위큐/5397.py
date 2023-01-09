import sys
input = sys.stdin.readline

def go(x):
    if x == '<':
        if not main_stack: return
        tmp_stack.append(main_stack.pop())
        return
    if x == '>':
        if not tmp_stack: return
        main_stack.append(tmp_stack.pop())
        return
    if x == '-':
        if not main_stack: return
        main_stack.pop()
        return
    main_stack.append(x)
    return


for _ in range(int(input())):
    S = input().rstrip()
    main_stack = []
    tmp_stack = []
    for s in S:
        go(s)
    while tmp_stack:
        main_stack.append(tmp_stack.pop())
    print(''.join(main_stack))