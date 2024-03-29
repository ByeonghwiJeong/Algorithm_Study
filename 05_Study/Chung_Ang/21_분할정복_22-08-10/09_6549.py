'''
히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램 작성

입력)
    - 1 : 직사각형의 수 n ~ [1, 100000], h1, h2, ... , hn
        [0, 1,000,000,000]
    - 2 : .... 동일
    - n : 0 >>> 종료!!!

< 스택을 이용하는 풀이 >
배열의 왼쪽 부터 탐색을 시작
스택의 최솟값에 대한 정보를 계속 유지
스택의 가장 위의 값보다 작은 값이 나온다면 그값을 pop
넓이의 최대값을 찾아감

'''
