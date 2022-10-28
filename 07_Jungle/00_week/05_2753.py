def yuncheck(a):
    if a % 400 == 0:
        return 1
    elif a % 100 == 0:
        return 0
    elif a % 4 == 0:
        return 1
    else:
        return 0

print(yuncheck(int(input())))