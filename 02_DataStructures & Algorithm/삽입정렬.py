'''

'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 2번째 요소부터 확인
    for j in range(i, 0, -1): # 인덱스 i ~~ 1
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그위치에서 break!
            break
print(array)