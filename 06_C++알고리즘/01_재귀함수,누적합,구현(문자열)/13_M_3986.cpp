/*
< 좋은단어 >
https://www.acmicpc.net/problem/3986
문제
- 좋은단어의 갯수를 찾아라!
- 좋은단어 : 같은 글자끼리 아치형 곡선으로 연결
    - 교차X 경우
*/
#include<bits/stdc++.h>
using namespace std;
int n, ret;
string s;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> s;
        stack<char> stk;
        for(char a : s){
            if(stk.size() && stk.top() == a) stk.pop();
            else stk.push(a);
        }
        if(stk.size() == 0) ret++;
    }
    cout << ret << "\n";
    return 0;
}
/*
- 기본적인 stack문제
- 자료구조 : stack<char> stk
*/
