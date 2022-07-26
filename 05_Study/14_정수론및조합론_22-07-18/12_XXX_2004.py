'''
25 C 12
n C r


5 C 2
5 4 3 2 1  5!
2 1 3 2 1  2!(5-2)!

n n-1 n-2 ... n-r-1
r r-1 r-2 ... 1

n!
------
r! (n-r)!
'''
import sys
input = sys.stdin.readline

def cnt_num(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

N, M = map(int, input().split())
five_cnt = cnt_num(N, 5) - cnt_num(M, 5) - cnt_num(N - M, 5)
two_cnt = cnt_num(N, 2) - cnt_num(M, 2) - cnt_num(N - M, 2)
print(min(five_cnt, two_cnt))