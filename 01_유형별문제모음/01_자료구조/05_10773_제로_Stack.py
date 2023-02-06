'''
자료구조 : Stack
- 삽입/삭제 연산 : 시간복잡도 O(1)
'''
import sys

N = int(sys.stdin.readline().rstrip())
_list = []
for i in range(N):
    tmp = int(sys.stdin.readline().rstrip())
    if tmp == 0:
        _list.pop()
    else:
        _list.append(tmp)

print(sum(_list))