'''
666은 종말을 나타내는 숫자라고 한다,
666이 있는 종말 숫자를 탐색
'''
N = int(input())
cnt = 0
i = 1
while True: 
    if '666' in str(i):
        cnt += 1
        if cnt == N:
            print(i)
            break
    i += 1
        