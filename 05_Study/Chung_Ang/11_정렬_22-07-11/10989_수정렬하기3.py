'''
메모리 초과 발생
숫자의 개수 : 1000만
숫자 범위 : 1만 이하 자연수
'''
import sys
input = sys.stdin.readline

# l = []
# for _  in range(int(input())):
#     l.append(int(input()))
# l.sort()
# print(*l, sep='\n')
'''
위 코드가 안되는 이유?
'''
l = {}
N = int(input())
for _ in range(N):
    i = int(input())
    if i in l:
        l[i] += 1
    else:
        l[i] = 1

for k, v in sorted(l.items()):
    for _ in range(v):
        print(k)