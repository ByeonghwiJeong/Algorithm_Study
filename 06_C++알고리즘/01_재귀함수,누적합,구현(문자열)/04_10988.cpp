/*
< 팰린드롬인지 확인하기 >
https://www.acmicpc.net/problem/10988
문제
- 팰린드롬(앞뒤대칭)문자열 확인
*/
#include<bits/stdc++.h>
using namespace std;
string s,temp;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> s;
    temp = s;
    reverse(temp.begin(), temp.end());
    if(temp == s) cout << 1 << "\n";
    else cout << 0 << "\n";
    return 0;
}
// reverse() 함수 사용법