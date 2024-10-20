import sys
input = sys.stdin.readline
N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]

# x좌표 기준 정렬
blocks.sort()

# 가장 높은 기둥의 인덱스를 찾는다.
max_height, max_height_index = max((block[1], i) for i, block in enumerate(blocks))

result = 0

# 왼쪽 부분 면적 계산 (가장 높은 기둥 전까지)
left_height = blocks[0][1]
for i in range(max_height_index):
    if blocks[i+1][1] > left_height:
        result += left_height * (blocks[i+1][0] - blocks[i][0])
        left_height = blocks[i+1][1]
    else:
        result += left_height * (blocks[i+1][0] - blocks[i][0])

# 오른쪽 부분 면적 계산 (가장 높은 기둥 이후)
right_height = blocks[-1][1]
for i in range(N-1, max_height_index, -1):
    if blocks[i-1][1] > right_height:
        result += right_height * (blocks[i][0] - blocks[i-1][0])
        right_height = blocks[i-1][1]
    else:
        result += right_height * (blocks[i][0] - blocks[i-1][0])

# 가장 큰 기둥의 면적 추가
result += max_height

# 결과 출력
print(result)
