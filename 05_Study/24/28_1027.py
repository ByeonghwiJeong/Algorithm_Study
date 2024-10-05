# 입력 처리
N = int(input())
heights = list(map(int, input().split()))

# i에서 j로 가는 기울기를 계산하는 함수
def slope(i, j):
    return (heights[j] - heights[i]) / (j - i)

max_visible = 0

for i in range(N):
    visible_count = 0
    
    # 왼쪽 빌딩들을 검사
    max_slope = float('-inf')
    for j in range(i - 1, -1, -1):
        current_slope = slope(j, i)
        if current_slope > max_slope:
            visible_count += 1
            max_slope = current_slope
    
    # 오른쪽 빌딩들을 검사
    max_slope = float('-inf')
    for j in range(i + 1, N):
        current_slope = slope(i, j)
        if current_slope > max_slope:
            visible_count += 1
            max_slope = current_slope
    
    # 현재 빌딩에서 볼 수 있는 빌딩 수를 갱신
    max_visible = max(max_visible, visible_count)

# 결과 출력
print(max_visible)
