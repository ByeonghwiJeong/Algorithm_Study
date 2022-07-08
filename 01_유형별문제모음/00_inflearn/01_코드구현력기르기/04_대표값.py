import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
min_value = 2147000000 # 정수형 크기에서 제일 작은값
ave = round(sum(scores) / N + 0.0001)

for i, score in enumerate(scores):
  interval = abs(score-ave)
  if interval < min_value:
    min_value = interval
    res_score = score
    min_index = i 
  elif interval == min_value:
    if score > res_score:
      res_score = score
      min_index = i

print(ave, min_index+1)