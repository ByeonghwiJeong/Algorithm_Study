/*
< 균형잡힌 세상 >
https://www.acmicpc.net/problem/4949
문제 
- 유효한 괄호(2종류)인지 확인
입력
1   : 여러줄에 걸처서 문자열
입력종료 조건 : "." 점하나
*/
#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    while(true){
        string s;
        getline(cin, s);
        if(s == ".") break;
        stack<int> stk;
        bool check = true;
        for(int i = 0;  s.length(); i++){
            if(s[i] == ')'){
                if(stk.size() == 0 || stk.top() == '['){
                    check = false;
                    break;
                }else{
                    stk.pop();
                }
            }
            if(s[i] == ']'){
                if(stk.size() == 0 || stk.top() == '('){
                    check = false;
                    break;
                }else{
                    stk.pop();
                }
            }
            if(s[i] == '(') stk.push(s[i]);
            if(s[i] == '[') stk.push(s[i]);
        }
        if(check && stk.size() == 0) cout << "yes\n";
        else cout << "no\n";
    }
    return 0;
}
/*
짝짓기 >>> 스택
*/
