import sys
input = sys.stdin.readline

def stack(s, x = 'x'):
    global _list
    if s == 'push':
        _list.append(x)
    elif s == 'pop':
        if _list:
            print(_list.pop())
        else:
            print('-1')
    elif s == 'size':
        print(len(_list))
    elif s == 'empty':
        if _list:
            print(0)
        else:
            print(1)
    elif s == 'top':
        if _list:
            print(_list[-1])
        else:
            print(-1)
            
_list = []
for _ in range(int(input())):
    _in = input().split()
    stack(*_in)

    