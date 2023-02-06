max_name = ['',0,0,2011]
min_name = ['',0,0,1980]

for _ in range(int(input())):
    x = input().split()
    for i in range(1, 4):
        x[i] = int(x[i])
    if max_name[3] > x[3]:
        max_name = x.copy()
    elif max_name[3] == x[3]:
        if max_name[2] > x[2]:
            max_name = x.copy()
        elif max_name[2] == x[2] and max_name[1] > x[1]:
            max_name = x.copy()
    if min_name[3] < x[3]:
        min_name = x.copy()
    elif min_name[3] == x[3]:
        if min_name[2] < x[2]:
            min_name = x.copy()
        elif min_name[2] == x[2] and min_name[1] < x[1]:
            min_name = x.copy()
            
print(min_name[0])
print(max_name[0])




