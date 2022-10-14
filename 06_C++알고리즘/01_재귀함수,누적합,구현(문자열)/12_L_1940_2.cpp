/*
200000이 넘은경우 예외처리
- 재료 2개를 합쳤을 때 최대값이 200000
- 이런 조건을 넣지 않더라도 통과할 수 있지만
- 이런 디테일을 챙기는것이 중요!
- 계산하지않아도 되는 조건을 따로 만들어준다
- 아주 조금 더 빨리진다!!!
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
    if(m > 200000) cout << 0 << "\n";
    else{
        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                if(a[i] + a[j] == m) cnt++;
            }
        }
        cout << cnt << "\n";
    }
    return 0;
}
/*

*/
