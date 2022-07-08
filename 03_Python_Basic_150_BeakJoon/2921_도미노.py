'''
1. 도미노 조각은 두칸으로 이루어져 있다.
2. 점의 개수는 세트의 크기에 의해 결정
3. 세트 크기가 N인 도미노 세트에서 점의 개수는 0 <=  <= N 이다



'''
N = int(input())
sum = 0
for i in range(N+1):
    for j in range(i+1):
        sum += i + j
print(sum)
