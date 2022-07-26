'''
덩치 > 키 & 몸무게
tuple 형태로 (키, 몸무게)

서로비교서 키와 몸무게 두 값이 둘다 커야 덩치가 크다

자신보다 덩치가 큰사람이 k명일때 덩치등수 k등

'''
l = []
N = int(input())
for _ in range(N):
    l.append(tuple(map(int, input().split())))
ans = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        elif l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            cnt += 1
    ans.append(cnt)
print(*ans)