/*
< printf >
- 형식을 지정해서 출력할 때 좋음
- 문자열 출력시 cout 좋음, c_str()를 통해 printf로도 출력 가능
- %'변수유형'
    - d : int, c : char, s : string
    - lf : double, ld : long long
예) "홍철 1: 지수 2" 출력
print("홍철 %d: 지수 %d", a, b)

----------
소수점 6자리 출력
- printf(".6lf\n", a);
2를 02로 만들어서 출력
- printf("%02d\n", b);
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
double a = 1.23456789;
int b = 2;
int main(){
    printf("%.6lf\n", a);
    printf("%02d\n", b);
    // 1.234568
    // 02
    return 0;
}