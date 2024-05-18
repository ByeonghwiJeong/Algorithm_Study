import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(line, L):
    # 경사로 Check
    visited = [0] * N
    for i in range(N-1):
        # 높이 같은 경우
        if line[i] == line[i+1]:
            continue
        # 높이 차이가 1 초과 
        if abs(line[i] - line[i+1]) > 1:
            return False
        # 현재height > 다음height 경우 오른쪽 높이가 같은지 체크
        if line[i] > line[i+1]:
            tmp = line[i+1] # 다음 높이
            for j in range(i+1, i+1+L):
                if 0 <= j < N:
                    # 경사 놓을 위치의 높이가 하나라도 다르면
                    if line[j] != tmp or visited[j]:
                        return False
                    # 경사 두기
                    visited[j] = 1
                # 경사 길이가 범위 초과
                else:
                    return False
        else:
            tmp = line[i]
            for j in range(i, i-L, -1):
                # 경사 길이 안이면
                if 0 <= j < N:
                    # 경사 놓을 위치의 높이가 하나라도 다르면, 이미 경사
                    if line[j] != tmp or visited[j]:
                        return False
                    # 경사 두기
                    visited[j] = 1
                # 경사 길이가 범위 초과
                else:
                    return False
    return True

answer = 0
# 가로길 체크
for i in range(N):
    if check(board[i], L):
        answer += 1

# 세로길 체크
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(board[j][i])
    if check(tmp, L):
        answer += 1

print(answer)
