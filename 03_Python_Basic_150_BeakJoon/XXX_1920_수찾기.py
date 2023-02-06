N = int(input())
l = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

l.sort()

def binary_check(start, end, target):
    if start == end:
        if l[start] == target:
            print(1)
        else:
            print(0)
        return
    half = (start + end) // 2
    if l[half] < target:
        binary_check(half+1, end, target)
    else:
        binary_check(start, half, target)


for target in check:
    binary_check(0, N-1, target)