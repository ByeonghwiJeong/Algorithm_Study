import sys
input = sys.stdin.readline

def is_stack(S):
    _list = []
    for s in S:
        if s == '(':
            _list.append(1)
        else:
            try:
                _list.pop()
            except:
                return 'NO'
    if _list:
        return 'NO'
    return 'YES'


for _ in range(int(input())):
    VPS = input().rstrip()
    print(is_stack(VPS))

