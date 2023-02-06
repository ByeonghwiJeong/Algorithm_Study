A = int(input())
B = int(input())
list = []
for i in range(1, 101):
    if A <= i**2 and i**2 <= B:
        list.append(i**2)
if list:  
    print(sum(list))
    print(min(list))
else:
    print(-1)