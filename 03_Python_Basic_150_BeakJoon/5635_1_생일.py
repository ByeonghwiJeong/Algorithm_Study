list = []
for i in range(int(input())):
    x = input().split()
    for i in range(1, 4):
        x[i] = int(x[i])
    list.append(x)
list.sort(key = lambda x:(x[-1], x[-2], x[-3]))
print(list[-1][0], list[0][0], sep='\n')