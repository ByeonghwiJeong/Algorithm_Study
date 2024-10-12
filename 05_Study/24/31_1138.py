'''
https://www.acmicpc.net/problem/1138
제목 : 한 줄로 서기

내용)
- N명의 사람들은 매일 아침 한 줄로 섬
- 1 ~ N 전부 키가 다르다
- 사람들은 자기보다 큰사람이 왼쪽에 몇 명 있었는지만 기억

입력 1)
4
2 1 1 0
출력 1)
4 2 1 3

입력 2)
5
0 0 0 0 0
출력 2)
1 2 3 4 5

'''
import sys
input = sys.stdin.readline

N = int(input())
tall_data = list(map(int, input().split()))

result = [0] * N

# for i in range(1, N + 1):
#     # 사람 i
#     left_cnt = tall_data[i - 1]
#     cnt = 0
#     for j in range(N):
#         if not result[j]:
#             # 빈자리 찾으면 cnt 증가
#             if cnt == left_cnt:
#                 result[j] = i
#                 break
#             cnt += 1


for i, left_cnt in enumerate(tall_data, start=1):
    # i : 사람번호
    # left_cnt : i번 왼쪽에 더 큰 사람수 
    for j in range(N):
        if result[j] == 0: # 빈자리 찾으면
            if left_cnt == 0:
                result[j] = i
                break
            left_cnt -= 1

print(*result)