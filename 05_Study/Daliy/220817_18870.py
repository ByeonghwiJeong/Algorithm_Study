'''
수직선 위에 N개의 좌표가 있다.
좌표압축 Yi
    - Yi는 Xi>Xj를 만족하는 서로 다른 좌표의 개수

'''
import sys
input = sys.stdin.readline

N = int(input())
_list = list(map(int, input().split()))
_sort = sorted(list(set(_list)))
_dict = dict()

cnt = 0
for i in _sort:
    _dict[i] = cnt
    cnt += 1

for i in _list:
    print(_dict[i], end=' ')
