'''
리스트로는 풀수 없다.
remove와 append가 시간복잡도 O(N)이다
자료구조 set()을 사용하고
add와 discard를 사용하면 시간복잡도 O(1)이다

S = set([i for i in range(1, 21)])
set이랑 표현식을 같이 사용하려면 
list 표현식을 먼저 선언한다.
'''
import sys
input = sys.stdin.readline

S = set()
for _ in range(int(input())):
    c = input().split()
    if len(c) == 1:
        command = c[0]
        if command == 'all':
            S = set([i for i in range(1, 21)])
        elif command == 'empty':
            S = set()
    else:
        command, num = c[0], int(c[1])   
        if command == 'add':
            S.add(num)
        elif command == 'remove':
            S.discard(num)
        elif command == 'check':
            if num in S:
                print(1)
            else:
                print(0)
            # print(1 if num in S else 0)
        elif command == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)

    