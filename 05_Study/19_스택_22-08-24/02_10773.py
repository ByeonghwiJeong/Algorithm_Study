import sys
input = sys.stdin.readline

def stack(x):
    global _list
    if x == 0:
        _list.pop()
    else:
        _list.append(x)

_list = []
for _ in range(int(input())):
    stack(int(input()))
print(sum(_list))