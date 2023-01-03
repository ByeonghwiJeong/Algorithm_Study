import sys
input = sys.stdin.readline

def sum_digit(x):
    res = 0
    for i in x:
        if i.isdigit(): res += int(i)
    return res

a = [input().rstrip() for _ in range(int(input()))]
a.sort(key= lambda x: (len(x), sum_digit(x), x))
print(*a, sep='\n')