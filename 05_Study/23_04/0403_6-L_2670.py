'''
<  연속부분최대 곱 >
https://www.acmicpc.net/problem/2670
문제)
- N개의 실수가 주어짐
- 한 개 이상의 연속된 수의 곱이 최대가 되는 부분을 찾아, 그 곱을 출력
입력)
- 1      : 양의 실수들의 개수 N ~ [1 \ 10000]
- 2[N]   : 양의 실수들 ~ [0.0 \ 9.9]
출력)
- 1      : 최대 곱, 소수점 이하 3자리까지 출력, 반올림
'''
import sys
input = sys.stdin.readline

N = int(input())
a = [float(input()) for _ in range(N)]
tmp = a[0]
ret = tmp
for i in range(1, N):
    if a[i] > tmp * a[i]: tmp = a[i]
    else: tmp *= a[i]
    ret = max(ret, tmp)
# 틀림
# print(round(ret, 3))
# 정답
# print("%.3f" % ret)
# ?
print(f'{ret:.3f}')

'''
# 틀림
# print(round(ret, 3))
# 정답
# print("%.3f" % ret)
# ?
print(f'{ret:.3f}')
'''