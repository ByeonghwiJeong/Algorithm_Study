# 메모이제이션 xxx 
# 단순 재귀 함수로 선언하면 지수 시간  복잡도
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