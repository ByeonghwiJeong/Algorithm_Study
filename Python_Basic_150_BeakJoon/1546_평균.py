N = int(input())
list = list(map(int, input().split()))
print(sum(list)/max(list)*100/N)
