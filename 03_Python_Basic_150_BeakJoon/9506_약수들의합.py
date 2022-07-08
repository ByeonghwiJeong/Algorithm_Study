while True:
    n = int(input())
    if n == -1:
        break
    sum_check = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sum_check.append(i)
    if n == sum(sum_check):
        # ans = f'{n} = 1 '
        # for i in range(1, len(sum_check)):
        #     ans += f'+ {sum_check[i]} '
        ans = f'{n} = ' + ' + '.join(str(i) for i in sum_check)
        print(ans)
        
    else:
        print(f'{n} is NOT perfect.')