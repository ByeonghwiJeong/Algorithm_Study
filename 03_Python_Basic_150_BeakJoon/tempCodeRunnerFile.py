S = []
for _ in range(int(input())):
    c = input().split()
    if len(c) == 1:
        command = c[0]
        if command == 'all':
            S = [i for i in range(1, 21)]
            continue
        elif command == 'empty':
            S = []
            continue
    else:
        command, num = c[0], c[1]   
        if command == 'add':
            if not num in S:
                S.append(num)
            continue
        elif command == 'remove':
            if num in S:
                S.remove(num)
            continue
        elif command == 'check':
            if num in S:
                print(1)
            else:
                print(0)
            continue
        elif command == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.append(num)
            continue
    