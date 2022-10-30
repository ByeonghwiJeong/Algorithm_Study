N = int(input())
cnt = 0
i = 1
while True: 
    if '666' in str(i):
        cnt += 1
        if cnt == N:
            print(i)
            break
        print(i)
    i += 1