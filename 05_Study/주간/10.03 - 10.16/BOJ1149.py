'''
< 수리공 항승>
https://www.acmicpc.net/problem/1449

'''
N, L = map(int, input().split())
holes = list(map(int, input().split()))
chk_holes = [False] * 1001
for i in holes:
    chk_holes[i] = True

cnt = 0
x = 0
while x < 1001:
    if chk_holes[x]:
        cnt += 1
        x += L
    else:
        x += 1
print(cnt)
