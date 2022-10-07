/*
< 농구 경기 >
https://www.acmicpc.net/problem/1159
문제
- 선수의 수 N ~ [1 \ 150]
- N개의 줄에는 선수의 성이 주어진다.
- 같은 성을 가진 선수가 5명 이상있을때 경기 진행
  - 선발가능한 성을 사전순 공백없이 출력
- 없으면 기권후 "PREDAJA" 출력
*/
#include<bits/stdc++.h>
using namespace std;
int n, cnt[26];
string s, ret;
int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> s;
        cnt[s[0] - 'a']++;
    }
    for(int i = 0; i < 26; i++) if(cnt[i] >= 5) ret += i + 'a';
    if(ret.size()) cout << ret << '\n';
    else cout << "PREDAJA" << "\n";
    return 0;
}
/*
- 알파벳 방문처리시 자료구조 cnt[26]
- 출력할 string 변수 ret = 0 ~ 25 + 'a'
- string ret값있는지 확인 : if(ret.size())
*/