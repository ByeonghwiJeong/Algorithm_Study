# S : 주어진 리스트
# x : target
# target이 S에 없으면 -1
def binary_search(S, x):
    low = 0
    high = len(S) - 1
    location = -1
    cnt = 0
    while (low <= high and location == -1):
        mid = (low + high) // 2
        print(f'step{cnt} : low:{low}/mid:{mid}/high:{high}')
        cnt += 1
        if (x == S[mid]):
            location = mid
        elif (x < S[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return location
    
S = [-1, 5, 7, 8, 10, 11, 13]
x = 5
location = binary_search(S, x)
print('S = ', S)
print('x = ', x)
print('location = ', location)
