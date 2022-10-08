/*
< ROT13 >
https://www.acmicpc.net/problem/11655
문제
- ROT13 : 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
- "Beakjoon Online Judge"를 ROT13으로 암호화 
    - "Onrxwbba Bayvar Whqtr"
- 위 문자열을 다시 ROT13암호화하면 복호화됨
- 알파벳이 아닌 글자는 그대로 남아있다.

*/
#include<bits/stdc++.h>
using namespace std;
string s;
int main(){
    getline(cin, s);
    for(int i = 0; i < s.size(); i++){
        // 대문자인경우 65 ~ 90 
        if(s[i] >= 65 && s[i] <= 90){
            if(s[i] + 13 > 90) s[i] = s[i] + 13 - 26;
            else s[i] = s[i] + 13;
        }else if(s[i] >= 97 && s[i] <= 122){
            if(s[i] + 13 > 122) s[i] = s[i] + 13 - 26;
            else s[i] = s[i] + 13;
        }
        cout << s[i];
    }
    return 0;
}
/*
- 1 : 대문자인경우 65 <= s <= 90
- 2 :소문자인경우 97 <= s <= 122
- 위 2가지 경우에서 +13일때 90과 122를 초과하는경우 -26
*/