/*
< NBA 농구 >
https://www.acmicpc.net/problem/2852
문제 
- 골이 들어간 시간을 적는다.
- 농구 경기는 48분간 진행
- 팀번호 1  or  2
입력
1   : 골이 들어간 횟수 ~ N[1\100]
2-N : 팀번호(1 or 2) 시각(mm:ss)
출력
*/
#include<bits/stdc++.h>
using namespace std;
#define prev hwi
int n, o, A, B, asum, bsum;
string s, prev;
string print(int a){
    string d = "00" + to_string(a / 60);
    string e = "00" + to_string(a % 60);
    return d.substr(d.size() - 2, 2) + ":" + e.substr(e.size() - 2, 2);
}
int changeToInt(string a){
    return atoi(a.substr(0, 2).c_str()) * 60 + atoi(a.substr(3, 2).c_str());
}
void go(int &sum, string s){
    sum += changeToInt(s) - changeToInt(prev);
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> o >> s;
        if(A > B) go(asum, s);
        else if(B > A) go(bsum, s);
        o == 1 ? A++ : B++;
        prev = s;
    }
    if(A > B) go(asum, "48:00");
    else if(B > A) go(bsum, "48:00");
    cout << print(asum) << "\n";
    cout << print(bsum) << "\n";
    return 0;
}
/*
구현 문제
*/
