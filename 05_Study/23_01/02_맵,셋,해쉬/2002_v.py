'''
< 추월 >
문제) 터널에서 추월한 차량 잡기
입력)
- 2N+1 개의 줄
- 1     : 차의 대수 N [1 \ 1000]
- 2[N]  : 차량 번호 목록 - in
- 3[N]  : 차량 번호 목록 - out
'''
import sys
input = sys.stdin.readline

n = int(input())
car_in = dict()
for i in range(n):
    car = input().rstrip()
    car_in[car] = i  # 들어가는 순서 저장

car_out = [input().rstrip() for _ in range(n)]

# 나오는 차량의 인덱스
# 들어간 차량의 인덱스
ans = 0
for i in range(n): 
    # 나오는 차 순서 (나오는 차가 추월 차량인지 check)
    for j in range(i+1, n): # 나온 차 기준으로 뒤에 차
        if car_in[car_out[i]] > car_in[car_out[j]]:
            ans += 1
            break

print(ans)


'''
< 추월 차량 판단 기준 >
1. 차량을 기준으로 들어간 순서를 해쉬맵 시킨다. 
- python dictionary 
key는 차량이름, value는 순서 
2. 우선 나오는 차량을 기준으로 잡고 
    그 뒤에 있는 차량의 순서가 더 빠른경우(숫자가 작은경우)
    기준 잡은 차량은 추월차량으로 판단한다!!!

중복??
in  : 1 2 3 4
out : 4 1 2 3
'''