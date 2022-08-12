// void : 리턴하는 값이 없다.
// a함수가 전역변수 ret 값을 2로 바꿔줌
#include <bits/stdc++.h>
using namespace std;
int ret = 1;
void a(){
    ret = 2;
    cout << ret << "\n";
    return;
}
int main(){
    a();
    return 0;
}