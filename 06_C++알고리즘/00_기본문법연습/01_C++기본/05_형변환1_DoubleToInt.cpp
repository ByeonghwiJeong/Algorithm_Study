/*
< double to int > 
- 앞에 int로 선언

형과 형을 똑같이 해주어야 합니다.
 1:   int b = (int) ret * 100;
 2:   int c = (int) 100 * ret;
1번 케이스만 형변환!!! 순서 생각 잘하자!
*/
#include <bits/stdc++.h>
using namespace std;
int main(){
    double ret = 2.12345;
    int n = 2;
    int a = (int)round(ret / double(n));
    int b = (int) ret * 100;
    int c = (int) 100 * ret;
    cout << a << "\n"; // 1
    cout << b << "\n"; // 200
    cout << c << "\n"; // 212
}