'''
처리되지 않은 테이터 중 가장 작은 테이터를 선택해 맨앞에 있는 데이터와 바꾸는것을 반복
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i 
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j # min_index :가장 작은 원소의 인덱스
    array[i], array[min_index] = array[min_index], array[i]

print(array)