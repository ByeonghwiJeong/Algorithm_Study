/*
< 수학숙제 >
https://www.acmicpc.net/problem/2870
문제
- 숫자와 알파벳 소문자로 되어있는 글 ~ N줄
- 숫자를 모두 찾은 뒤, 내림차순으로 정리해야한다.
- 숫자 앞에 0이 있는 경우에는 정리하면서 생략할 수 있다.
*/
#include<bits/stdc++.h>
using namespace std;
int n;
string ret, s;
vector<string> v;
void go(){
    while(true){
        if(ret.size() && ret.front() == '0') ret.erase(ret.begin());
        else break;
    }
    if(ret.size() == 0) ret = "0";
    v.push_back(ret);
    ret = "";
}
bool cmp(string a, string b){
    if(a.size() == b.size()) return a < b;
    return a.size() < b.size();
}
int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> s;
        ret = "";
        for(int j = 0; j < s.size(); j++){
            if(s[j] < 65) ret += s[j];
            else if(ret.size()) go();
        }
        if(ret.size()) go();
    }
    sort(v.begin(), v.end(), cmp);
    for(string i : v) cout << i << "\n";
    return 0;
}