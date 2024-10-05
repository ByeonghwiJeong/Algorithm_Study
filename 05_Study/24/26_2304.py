import sys
input = sys.stdin.readline
N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]

# x좌표 기준 정렬
blocks.sort(key=lambda x: x[0])

# 가장 높은 기둥 찾기
max_height = max(blocks, key=lambda x: x[1])
max_height_index = blocks.index(max_height)

# 면적 계산 함수
def cal_area(stack: list) -> int:
    area = 0
    for i in range(len(stack) - 1):
        width = abs(stack[i+1][0] - stack[i][0])
        height = stack[i][1]
        area += width * height
    return area

# 왼쪽 영역 계산
left_stack = [blocks[0]]  # 왼쪽에서 시작
for i in range(1, max_height_index + 1):
    if blocks[i][1] > left_stack[-1][1]:
        left_stack.append(blocks[i])
    elif blocks[i][1] == left_stack[-1][1]:
        left_stack[-1] = blocks[i]  # 동일 높이에서는 오른쪽으로 확장

left_area = cal_area(left_stack)

# 오른쪽 영역 계산
right_stack = [blocks[-1]]  # 오른쪽에서 시작
for i in range(N-2, max_height_index - 1, -1):
    if blocks[i][1] > right_stack[-1][1]:
        right_stack.append(blocks[i])
    elif blocks[i][1] == right_stack[-1][1]:
        right_stack[-1] = blocks[i]  # 동일 높이에서는 왼쪽으로 확장

right_area = cal_area(right_stack)

# 결과 출력 (왼쪽 영역 + 가장 큰 기둥의 면적 + 오른쪽 영역)
print(left_area + max_height[1] + right_area)