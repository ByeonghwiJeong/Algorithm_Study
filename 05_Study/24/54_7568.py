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



# 입력 처리
N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]

# 등수 계산
ranks = []
for i, (weight_i, height_i) in enumerate(people):
    rank = 1  # 기본 등수는 1
    for j, (weight_j, height_j) in enumerate(people):
        if i != j and weight_i < weight_j and height_i < height_j:
            rank += 1  # 자신보다 덩치가 큰 사람이 있을 경우 등수 증가
    ranks.append(rank)

# 결과 출력
print(*ranks)