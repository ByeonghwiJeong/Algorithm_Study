/*
< 일곱 난쟁이 >
https://www.acmicpc.net/problem/2309
문제
- 9명의 난쟁이의 키가 주어진다.
- 7명의 합이 100일때 진짜 난쟁이의 키를 오름차순 출력
*/
#include<bits/stdc++.h>
using namespace std;
int a[9], sum;
vector<int> v;
pair<int, int> ret;
void solve(){
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < i; j++){
            if(sum - a[i] - a[j] == 100){
                ret = {i, j};
                return;
            }
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    for(int i = 0; i < 9; i++){
        cin >> a[i];
        sum += a[i];
    }
    solve();
    for(int i = 0; i < 9; i++){
        if(ret.first == i || ret.second == i) continue;
        v.push_back(a[i]);
    }
    sort(v.begin(), v.end());
    for(int i : v) cout << i << "\n";
    return 0;
}
/*
ALL합 - a - b == 100 ???
solve() >> 9C2 구현
*/