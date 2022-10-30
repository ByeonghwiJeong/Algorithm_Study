/*
< 괄호 >
https://www.acmicpc.net/problem/9012
문제 
- 유효한 괄호인지 확인 
입력
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
출력
NO
NO
YES
NO
YES
NO
*/
#include<bits/stdc++.h>
using namespace std;
int n;
string s;
bool check(string s){
    stack<char> stk;
    for(char c : s){
        if(c == '(') stk.push(c);
        else{
            if(!stk.empty()) stk.pop();
            else return false;
        }
    }
    return stk.empty();
}
int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> s;
        if(check(s)) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}
/*
짝짓기 >>> 스택
*/
