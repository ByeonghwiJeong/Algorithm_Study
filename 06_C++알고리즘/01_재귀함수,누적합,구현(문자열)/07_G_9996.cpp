/*
< 한국이 그리울 땐 서버에 접속하지 >
https://www.acmicpc.net/problem/9996
문제
- 첫번째 줄 : 파일의 개수 N
- 두번째 줄 : 패턴이 주어진다.
    - 소문자 여러개와 별표(*)하나로 이루어진 문자열
    - 별표(*) : 알파벳 소문자로 이루어진 임의의 문자열
        - 아스키 : 42
- 세번째 줄[N] : N개의줄에 파일이름
- 출력 : 일치-"DA", 불일치-"NE"
*/
#include<bits/stdc++.h>
using namespace std;
int n;
string s, ori_s, pre, suf;
int main(){
    cin >> n;
    cin >> ori_s;
    int pos = ori_s.find('*');
    pre = ori_s.substr(0, pos);
    suf = ori_s.substr(pos + 1);
    for(int i = 0; i < n; i++){
        cin >> s;
        if(pre.size() + suf.size() > s.size()){
            cout << "NE\n";
        }else{
            if(pre == s.substr(0, pre.size()) && suf == s.substr(s.size() - suf.size())) cout << "DA\n";
            else cout << "NE\n";
        }
    }
    return 0;
}
/*
- 문자열 처리 (문자검색) : string.find('*')
    - index 반환
    - 없을경우 string::npos 반환
- * 을 중심으로 앞pre뒤suf로 자른다
- 패턴이 더 큰경우 예외처리 : 불일치 반례
    - 이런경우를 따로 생각해야함
- substr사용법
    - 2개 parameters a, b : a이상 b미만
    - 1개 parameter c : C부터 끝까지 
- pre == s.substr(0, pre.size())
    - 앞부분 일치 확인
- suf == s.substr(s.size() - suf.size())
    - 뒤부분 일치 확인

*/