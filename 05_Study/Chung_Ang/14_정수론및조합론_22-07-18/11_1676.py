'''
5
25
125
'''
import sys
input = sys.stdin.readline

chk = [0] * 501
for i in range(1, 501):
    if i % 5 == 0:
        chk[i] += 1
    if i % 25 == 0:
        chk[i] += 1
    if i % 125 == 0:
        chk[i] += 1

N = int(input())
print(sum(chk[1:N+1]))