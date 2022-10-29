'''
정렬하기
1순위 : 갯수
2순위 : 입력 순서-같은수중첫번째로 들어오는 순서만체크
>>> (값, 갯수, 순서) : tuple형태로 만들기
'''
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
a = list(map(int, input().split()))
cnt_dict = dict()
_order = list()
for i in a:
    if not i in _order: _order.append(i)
print(*sorted(a, key=lambda x: (-a.count(x), _order.index(x))))

