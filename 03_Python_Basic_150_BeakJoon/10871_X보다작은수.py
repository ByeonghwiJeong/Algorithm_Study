N, X = map(int, input().split())
list = list(map(int, input().split()))
ans = [str(x) for x in list if x < X]
print(' '.join(ans))