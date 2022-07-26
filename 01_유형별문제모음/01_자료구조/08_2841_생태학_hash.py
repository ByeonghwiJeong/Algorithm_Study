'''
미국 전역의 나무들이 주어졌을때
각 종이 전체에서 몇 %를 차지하는지 구하시오
입력)
    - 한줄에 하나의 나무 종 이름
    - 최대 10,000개의 종
    - 최대 1,000,000그루의 나무
from collections import defaultdict
_dict = defaultdict(int)
_dict['abc'] += 1
    >>> 기본 value 0으로 초기화 후 +1

'''
import sys
input = sys.stdin.readline

_dict = dict()
cnt = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in _dict:
        _dict[tree] += 1
    else:
        _dict[tree] = 1
    cnt += 1

tree_list = list(_dict.keys())
tree_list.sort()
# print(tree_list)
for i in tree_list:
    # print(f'{i} {round(_dict[i]/cnt*100, 4)}')
    # round(0.5) > round(-0.5) >>> 0
    print(f'{i} {_dict[i]/cnt*100:.4f}')