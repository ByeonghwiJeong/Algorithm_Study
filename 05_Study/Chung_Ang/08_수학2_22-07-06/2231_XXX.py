'''
어떤 자연수 N에 대하여
그 자연수 N의 분해합은 
N과 N을 이루는 각 자리수의 합을 의미

예) 245 > 245 + 2 + 4 + 5 = 256
    245는 256의 생성자가 된다.
    특정 자연수는 생성자가 없을 수도 있다.
'''
N = int(input())
ans = 0
for i in range(1, N):
    ans = i
    # print(ans)
    a = list(map(int, str(i)))
    ans += sum(a)
    # print(ans)
    if ans == N:
        print(i)
        break
else:
    print(0)