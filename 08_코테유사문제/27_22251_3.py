'''
< 빌런 호석 > 
https://www.acmicpc.net/problem/22251
문제)
- 1 ~ N 이용 가능한 엘리베이터가 있다.
- 엘리베이터의 층수를 보여주는 디스플레이에는 최대 K자리수
- 수는 0으로 시작할 수도 있다.
- 0부터 9까지의 각 숫자가 디스플레이에 보이는 방식은 아래와 같다.
- 각 숫자는 7개의 표시등 중의 일부에 블이 들어오면서 표현
- 빌런 호석은 치르기 빌딩의 엘리베이터 디스플레이의 LED 중에서 \
    최소 1개, 최대 P개를 반전시킬 계획을 세우고 있다.
- 반전 : ON => OFF, OFF => ON
- 엘리베이터가 실제로 X층에 멈춰있을 때, \
    호석이가 반전시킬 LED를 고를 수 있는 경우의 수를 계산해보자.
입력)
- 1		: N 층수, K 디스플레이 자리스, P 최대 반전수, X 멈춰있는 층수 \
	- 1 <= X <= N < 10^K
	- 1 <= K <= 6
	- 1 <= P < 42
출력)
- 1		: 호석이가 반전시킬 LED를 고를 수 있는 경우의 수
- 
'''
import sys
input = sys.stdin.readline

nums = [
	0b1111110, # 0
	0b0110000, # 1
	0b1101101, # 2
	0b1111001, # 3
	0b0110011, # 4
	0b1011011, # 5
	0b1011111, # 6
	0b1110000, # 7
	0b1111111, # 8
	0b1111011, # 9
]

N, K, P, X = map(int, input().split())

res = 0
_origin  = str(X).zfill(K) # 35
for i in range(N+1):
	if i == X: continue # X층은 건너뛰기
	cnt = 0
	_to = str(i).zfill(K) # 1 ~ 48, 01 ~ 09
	for j in range(K):
		# for k in range(7):
		# 	if nums[int(_origin[j])][k] != nums[int(_to[j])][k]:
		# 		cnt += 1
		tmp = nums[int(_origin[j])] ^ nums[int(_to[j])]
		while tmp:
			if tmp & 1:
				cnt += 1
			tmp >>= 1
	if cnt <= P:
		res += 1

print(res)
