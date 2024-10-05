import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def count_ones(x):
    if x <= 0:
        return 0
    bit = 1
    cnt = 0
    while bit <= x:
        full_count = x // (bit * 2)
        reminder = x % (bit * 2)
        cnt += full_count * bit
        cnt += max(0, reminder - bit +  1)
        bit <<= 1
    return cnt

'''
[ 예시 (x = 12인 경우) ]
bit = 1 (가장 오른쪽 비트):
full_count = 12 // (1 * 2) = 6
reminder = 12 % (1 * 2) = 0
cnt += 6 * 1 = 6
cnt += max(0, 0 - 1 + 1) = 0
현재까지 cnt = 6
bit = 2 (두 번째 비트):
full_count = 12 // (2 * 2) = 3
reminder = 12 % (2 * 2) = 0
cnt += 3 * 2 = 6
cnt += max(0, 0 - 2 + 1) = 0
현재까지 cnt = 12
bit = 4 (세 번째 비트):
full_count = 12 // (4 * 2) = 1
reminder = 12 % (4 * 2) = 4
cnt += 1 * 4 = 4
cnt += max(0, 4 - 4 + 1) = 1
현재까지 cnt = 17
bit = 8 (네 번째 비트):
full_count = 12 // (8 * 2) = 0
reminder = 12 % (8 * 2) = 12
cnt += 0 * 8 = 0
cnt += max(0, 12 - 8 + 1) = 5
최종 cnt = 22
1  (   1)
2  (  10)
3  (  11)
4  ( 100)
5  ( 101)
6  ( 110)
7  ( 111)
8  (1000)
9  (1001)
10 (1010)
11 (1011)
12 (1100)
'''

print(count_ones(B) - count_ones(A-1))