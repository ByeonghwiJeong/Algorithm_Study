'''
리스트로는 풀수 없다.
remove와 append가 시간복잡도 O(N)이다
자료구조 set()을 사용하고
add와 discard를 사용하면 시간복잡도 O(1)이다
'''
S = []
for _ in range(int(input())):
    c = input().split()
    if len(c) == 1:
        command = c[0]
        if command == 'all':
            S = [str(i) for i in range(1, 21)]
            print(S)
        elif command == 'empty':
            S = []
    else:
        command, num = c[0], c[1]   
        if command == 'add':
            if not num in S:
                S.append(num)
        elif command == 'remove':
            if num in S:
                S.remove(num)
        elif command == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.append(num)

    