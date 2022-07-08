for _ in range(int(input())):
    N = int(input())
    total_sum = 0
    num = 0
    for _ in range(N):
        a, b = map(float, input().split())
        total_sum += a * b
        num += a
    print(int(num), round(total_sum / num, 1))