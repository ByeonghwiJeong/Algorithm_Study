/*
- reverse
원래의 문자열을 바꿔버립니다
begin과 end를 통해 전체를 바꿔도 되고
dopa.begin(), dopa.begin() + 3 이런식으로 부분만 바꿔버릴 수도 있습니다.

- substr
시작지점으로부터 몇개의 문자열을 뽑아냅니다.
(시작지점, 몇개) 이렇게 2개의 매개변수가 들어가게 됩니다. 
만약 시작지점만 넣게 되면 마지막까지 문자열을 뽑아냅니다.

- find
어떠한 문자열이 들어있나 찾습니다. 
만약 찾지 못한다면 문자열의 끝 위치인 string::npos를 반환
*/
#include <bits/stdc++.h>
using namespace std;
string dopa = "amumu is best";
int main(){
    cout << dopa << "\n";
    // amumu is best
    if(dopa.find("amumu") != string::npos){
        cout << "amumu in dopa!\n";
    }
    // amumu in dopa!
    cout << dopa.substr(0, 3) << "\n";
    // amu
    reverse(dopa.begin(), dopa.end());
    cout << dopa << "\n";
    // tseb si umuma
    return 0;
}