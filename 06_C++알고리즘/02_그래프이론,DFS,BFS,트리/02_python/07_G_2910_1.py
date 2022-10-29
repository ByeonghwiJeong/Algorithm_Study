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
order_dict = dict()
for i, v in enumerate(a):
    if not v in cnt_dict: cnt_dict[v] = 0
    cnt_dict[v] += 1
    if not order_dict.get(v): order_dict[v] = i + 1 
    # i에 0이들어가면 if not 한번 더 돌음 >> i + 1
a = list(set(a))
b = list()
for i in a:
    b.append((i, cnt_dict[i], order_dict[i]))
b.sort(key=lambda x: (-x[1], x[2]))
for t in b:
    for _ in range(t[1]):
        print(t[0], end=' ')
