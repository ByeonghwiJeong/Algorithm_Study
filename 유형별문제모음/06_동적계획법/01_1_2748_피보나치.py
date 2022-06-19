# 메모이제이션 xxx 
# cnt = 0
def f(n):
    # global cnt
    # cnt += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return f(n - 1) + f(n - 2)

print(f(int(input())))
# print(f'cnt: {cnt}')