/*
출력은 cout과 printf가 있습니다.

<cout>
일반적
- cout << 출력할것 << "\n";
답이 한칸 띄어쓰기를 원하면
- cout << 출력할것 << " "; 

< cout을 사용해 정수부분 + 소수부분 6자리 출력 >
- 소수부분은 반올림
- cout.precision(7);
*/
#include <bits/stdc++.h>
using namespace std;
double a = 1.23456789;
int main(){
    cout << a << "\n"; // 1.23457
    cout.precision(7);
    cout << a << "\n"; // 1.234568
}