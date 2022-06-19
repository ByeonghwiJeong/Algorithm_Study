'''
M x N = 500,000 x 500,000
>>> 시간 초과 발생
이분탐색을 이용해서 M x logN 로 적용해서 문제풀이 

'''
from bisect import bisect_left, bisect_right

N = int(input())
# _ = int(input())
# C ++은 N, M 이 필요함
cards = sorted(list(map(int, input().split())))
M = int(input())
# _ = int(input())
qry = list(map(int, input().split()))
ans = []
for q in qry:
    l = bisect_left(cards, q)
    r = bisect_right(cards, q)
    ans.append(1 if r - l else 0)
    # r - l 가 0이 아닌경우 1 반환

# for q in qry:
#     l = bisect_left(cards, q)
#     if cards[l] == q:
#         ans.append(1)
#     else:
#         ans.append(0)
for i in ans:
    print(i, end=' ')
# print(*ans)
# print(' '.join(map(str, ans)))