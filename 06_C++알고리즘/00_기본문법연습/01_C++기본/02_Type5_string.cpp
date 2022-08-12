/*
<문자열에서 + 연산은 "아스키코드"를 기반으로 수행>

숫자로 된 문자에서 1을 더해준다면
아스키 코드에서 +1 한 값이 됩니다

string s = "123"에서 s[0]의 값이 ++해주면
"223" 출력

<알파벳 : 26개>
대문자 A : 65, Z : 90
소문자 a : 97, z : 122

(int)'a' 하면 아스키코드 기반으로 97로 변환
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    string s = "123";
    char a = 'a';
    s[0]++;
    cout << s << "\n"; // 223
    cout << (int)a << "\n"; // 97
    return 0;
}