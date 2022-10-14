/*
< 주몽 >
https://www.acmicpc.net/problem/1213
문제
- 갑옷을 만드는 재료들은 각각의 고유번호가 있다.
- 갑옷은 두 개의 재료로 만드는데 두 재료의 고유번호를 M으로 합친다.
- N개의 재료가 주어졌을때
    - M갑옷을 만들 수 있는 개수
- 첫째줄 : N ~ [1 \ 15,000] 재료의 개수
- 둘째줄 : M ~ [1 \ 10,000,000] 갑옷을 만드는데 필요한 수
- 셋째줄[N] : N개의 고유번호 with 공백 ~ [1 \ 100,000]
*/
#include<bits/stdc++.h>
using namespace std;
int n, m, a[15001], cnt;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(a[i] + a[j] == m) cnt++;
        }
    }
    cout << cnt << "\n";
    return 0;
}
/*
배열 int a[15001] 정렬방법
- sort(a, a + n)
- n번째까지 정렬 
*/
