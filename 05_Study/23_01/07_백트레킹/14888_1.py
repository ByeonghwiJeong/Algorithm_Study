import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
_min = 987654321
_max = -987654321

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: int(x / y)

functions = [add, sub, mul, div]

def backtraking(cnt, val):
    global _max, _min
    if cnt == n:
        _max = max(_max, val)
        _min = min(_min, val)
        return
    
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            backtraking(cnt + 1, functions[i](val, nums[cnt]))
            operator[i] += 1
    return

backtraking(1, nums[0])
print(_max)
print(_min)