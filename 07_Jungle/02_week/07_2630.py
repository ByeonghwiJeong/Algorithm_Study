'''
< 색종이 만들기 >
https://www.acmicpc.net/problem/2630
문제)
- N x N 색종이 ~ [N = 2^k] k는 7이하의 자연수
- 4조각으로 나눌때 같은 색만있는 경우 
- 하얀색 색종이 개수, 파란색 색종이 개수
입력)
- 하얀색 0, 파란색 1
출력)
- 
'''
import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
w = b = 0
def equal_color(sr, sc, l):
    tmp = a[sr][sc]
    for i in range(sr, sr + l):
        for j in range(sc, sc + l):
            if a[i][j] != tmp: return False
    return True

def recur(sr, sc, l):
    global w, b
    if equal_color(sr, sc, l):
        if a[sr][sc]: b+= 1
        else: w += 1
    else:
        l //= 2
        mr = sr + l
        mc = sc + l
        recur(sr, sc, l)
        recur(sr, mc, l)
        recur(mr, sc, l)
        recur(mr, mc, l)
    return

recur(0, 0, n)
print(w)
print(b)


'''

'''