/*
string 으로 선언한 기존값a에 
+= 를 사용시 더할수 있으며
길이 출력시 a.size() 라는 메소드 사용
*/
#include <bits/stdc++.h>
using namespace std;
int main(){
    string a = "wow";
    a += " ";
    a += "fantastic";
    cout << a.size() << "\n";
    cout << a << "\n";
    return 0;
}