'''
질문 90% 정도에서 예외걸리는데 
'''

S = int(input())
tmp = int((2*S)**0.5) + 1
for i in range(tmp, 1, -1):
    if i*(i+1) < S*2:
        print(i)
        break
    elif i*(i+1) == S*2:
        print(i-1)
        break
