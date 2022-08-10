'''
1 ~ n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있
8 
4 3 6 8 7 5 2 1
+ 1
+ 1 2
+ 1 2 3
+ 1 2 3 4
- 1 2 3 / 4
- 1 2 / 4 3 
+ 1 2 5 / 4 3
+ 1 2 5 6 / 4 3
- 1 2 5 / 4 3 6
+ 1 2 5 7 / 4 3 6
+ 1 2 5 7 8 / 4 3 6
- 1 2 5 7 / 4 3 6 8
- 1 2 5 / 4 3 6 8 7
- 1 2 / 4 3 6 8 7 5
- 1 / 4 3 6 8 7 5 2
- / 4 3 6 8 7 5 2 1
'''

import sys
input = sys.stdin.readline

N = int(input())
_list = []
ans = []
cnt = 1
for _ in range(N):
    num = int(input())
    
    while cnt <= num:
        _list.append(cnt)
        ans.append('+')
        cnt += 1
    
    if num == _list.pop():
        ans.append('-')
    else:
        print('NO')
        break
else:
    print(*ans, sep='\n')