/*
< 알파벳 개수 >
https://www.acmicpc.net/problem/10808
문제
- 알파벳 소문자로만 이루어진 단어 S가 주어진다.
- 각 알파벳이 단어에 몇개가 포함되어 있는지 구하라
*/
#include<bits/stdc++.h>
using namespace std;
string str;
int cnt[26]; // 전역변수로 해야 0으로 초기화됨
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> str;
    for(char a : str) cnt[a - 'a']++; //'a'는 97로 자동변환
    for(int i = 0; i < 26; i++) cout << cnt[i] << " ";
    return 0;
}