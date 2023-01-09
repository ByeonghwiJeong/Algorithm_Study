'''
입력)
- 1     : N ~ [2 \ 11]
- 2     : A1, A2 ... An
- 3     : + - x / 개수 (합 N-1)
출력)
- 1     : 최댓값
- 2     : 최솟값
'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input()) # 숫자의 개수
a = list(map(int, input().split())) 
add, sub, mul, div = map(int, input().split())
_min = 987654321
_max = -987654321

# x: 갯수, r: 결과값
def dfs(x, r, x1, x2, x3, x4):
    global _min, _max
    if x == n:
        _min = min(_min, r)
        _max = max(_max, r)
        return
        
    if x1 > 0: dfs(x + 1, r + a[x], x1 - 1, x2, x3, x4)
    if x2 > 0: dfs(x + 1, r - a[x], x1, x2 - 1, x3, x4)
    if x3 > 0: dfs(x + 1, r * a[x], x1, x2, x3 - 1, x4)
    if x4 > 0: dfs(x + 1, int(r / a[x]), x1, x2, x3, x4 - 1)

dfs(1, a[0], add, sub, mul, div)
print(_max)
print(_min)


'''
나눗셈 조심할것!!!!
'''