'''
1. 수평 수직 이동 가능한 로봇 청소기
2. n x n 정사각형 청소
< 청소 방법>
    1) 처음에 수평 / 수직 방향 결정
        - 수평 : 열이 증가하는 방향
        - 수직 : 행이 증가하는 방향
    2) 1행 1열에서 시작
    3) 1)에서 설정한 방법으로 1칸 move
    4) 

수평 hrizontal = true

(0,0)
(0,1) (1,1) (1,0)
(2,0) (2,1) (2,2) (1,2) (0,2)  / n = 3
(0,3) (1,3) (2,3) (3,3) (3,2) (3,1) (3,0)

수직

(0,0)
(1,0) (1,1) (0,1)
(2,0) (2,1) (2,2) (1,2) (0,2)

'''
# horizontal = False
horizontal = True
coord = [(0,0)]
n = 5
for i in range(1, n):
    side_len = ((i+1)**2-i**2-1)//2 + 1
    cnt = 0
    if horizontal == True and i == 1:
        tmp = (0,1)
        coord.append(tmp)
        cnt += 1
    elif horizontal == False and i == 1:
        tmp = (1,0)
        coord.append(tmp)
        cnt += 1
    else:
        tmp_1 = coord[-1]
        # print(tmp_1)
        if tmp_1[0] == 0:
            tmp = (0,tmp_1[1]+1)
            coord.append(tmp)
            cnt += 1
        else:
            tmp = (tmp_1[0]+1,0)
            coord.append(tmp)
            cnt += 1
    # print('51tmp', tmp)
    if tmp[0] == 0:
        # print('54tmp', tmp)
        for i in range(1, side_len):
            tmp_1 = (tmp[0]+i,tmp[1])
            coord.append(tmp_1)
        tmp = coord[-1]
        for i in range(1, side_len):
            tmp_1 = (tmp[0],tmp[1]-i)
            coord.append(tmp_1)
    elif tmp[1] == 0:
        # print('60tmp', tmp)
        for i in range(1, side_len):
            tmp_1 = (tmp[0],tmp[1]+i)
            coord.append(tmp_1)
        tmp = coord[-1]
        for i in range(1, side_len):
            tmp_1 = (tmp[0]-i,tmp[1])
            coord.append(tmp_1)

print(coord)