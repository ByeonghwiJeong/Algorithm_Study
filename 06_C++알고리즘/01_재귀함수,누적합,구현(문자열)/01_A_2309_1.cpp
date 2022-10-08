/*
< 일곱 난쟁이 >
https://www.acmicpc.net/problem/2309
문제
- 9명의 난쟁이의 키가 주어진다.
자료구조 int a[9]
- 7명의 합이 100일때 진짜 난쟁이의 키를 오름차순 출력
*/
#include<bits/stdc++.h>
using namespace std;
int a[9];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    for(int i = 0; i < 9; i++){
        cin >> a[i];
    }
    sort(a, a + 9);
    do{
        int sum = 0;
        for(int i = 0; i < 7; i++) sum += a[i];
        if(sum == 100) break;
    }while(next_permutation(a, a + 9));
    for(int i = 0; i < 7; i++) cout << a[i] << "\n";
    return 0;
}