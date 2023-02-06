import sys
input = sys.stdin.readline

'''
1   6*0 + 1 i=1
    1 > 1
2   6*1 
    2 ~ 7 > 6 
3   6*2
    8 ~ 19 > 12 / 19=
4   6*3
    20 ~ 37 > 18
( 1, 2, 3 ... n ) * 6 >>> 3n(n + 1)+1 
'''
N = int(input())
i = 1
j = 0
while True:
    if N == 1:
        print(1)
        break
    if 1 < N <= 7:
        print(2)
        break
    if (3*j*(j + 1)+1) < N <= (3*i*(i + 1)+1):
        print(i+1)
        break
    i += 1
    j += 1
    

    