/*
<< 문자 <> 숫자 >>
- 문자를 숫자로 바꾸는 로직
- 아스키코드 이용
- A~Z : 65~90
- a~z : 97~122

< a~z 를 0~26으로 표현 >
1:  cout << (int)a - 97 << "\n";
2:  cout << (int)a - 'a' << "\n";
1번 2번 같은 뜻!
*/
#include <bits/stdc++.h>
using namespace std;
int main(){
    char a = 'a';
    cout << (int)a - 97 << "\n";
    cout << (int)a - 'a' << "\n";
    return 0;
}