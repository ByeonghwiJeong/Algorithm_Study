import sys
input = sys.stdin.readline

def is_stack(S):
    _list = []
    try:
        for s in S:
            if s == '(':
                _list.append(1)
            elif s == '[':
                _list.append(2)
            elif s == ')':
                    if _list[-1] == 1:
                        _list.pop()
                    else:
                        return 'no'
            elif s == ']':
                    if _list[-1] == 2:
                        _list.pop()
                    else:
                        return 'no'
    except:
        return 'no'
    if _list:
        return 'no'
    return 'yes'

while True:
    S = input().rstrip()
    if S == '.':
        break
    print(is_stack(S))
    