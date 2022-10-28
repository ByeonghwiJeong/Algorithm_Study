'''
<종이 자르기>
https://www.acmicpc.net/problem/2628

입력
- 1 : 가로, 세로 (자연수) ~ [1 \ 100]
- 2 : 칼로 잘라야하는 점선의 개수
- 3 : 가로 - 0 and 번호 // 세로 - 1 and 번호

'''
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
x1 = [0, x]
y1 = [0, y]
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 0:
        y1.append(b)
    else:
        x1.append(b)
x1.sort()
y1.sort()
x2 = [x1[i+1] - x1[i] for i in range(len(x1)-1)]
y2 = [y1[i+1] - y1[i] for i in range(len(y1)-1)]
print(max(x2) * max(y2))
