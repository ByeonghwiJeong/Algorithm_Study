'''
< 하늘에서 별똥별이 빗발친다 >
문제)
- 하늘에서 별똥별이 떨어진다.
- LxL 트램펄린으로 별동별이 떨어지는걸 막으려한다.
- 최대한 많은 별똥 별을 튕겨내도록 배치했을 때, 지구 충돌 별동별 수?
입력)
- 1     : N, M, L, K
    - N, M : 별똥별이 떨어지는 구역의 가로길이, 세로길이 ~ [1 \ 500,000]
    - L : 트램펄린 한변의 길이 ~ [1 \ 100,000]
    - K : 별똥별의 수
- 2[K]  : 별똥별 떨어지는 x, y좌표 ~ [0 \ N,M]
'''
import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(k)]

def calc(x, y):
    global ret
    cnt = 0
    for i in range(k):
        if x <= a[i][0] <= x + l and y <= a[i][1] <= y + l : cnt += 1
    ret = max(ret, cnt)

ret = 0
# 별동별 2개 정해주기
# 하나는 x좌표 다른 하나는 y좌표
for i in range(k):
    for j in range(k):
        calc(a[i][0], a[j][1])
print(k-ret)