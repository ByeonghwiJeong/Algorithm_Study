#include<bits/stdc++.h>
using namespace std;
string dopa = "life is limited";
int main(){
    cout << dopa << "\n";
    // 문자열에서 부분배열(이 부분만을 GET)
    cout << dopa.substr(0, 3) << "\n";
    // 반대로
    reverse(dopa.begin(), dopa.end());
    cout << dopa << "\n";
    // 추가한다
    dopa += "dopa!";
    cout << dopa << "\n";
    return 0;
}
/*
life is limited
lif
detimil si efil
detimil si efildopa!
*/

