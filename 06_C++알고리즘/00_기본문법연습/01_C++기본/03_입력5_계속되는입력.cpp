/*
입력을 계속주다가 안줄 때 끝나는 경우

<1안>
while(scanf("%d", &n) != EOF)
<2안>
while(cin >> n) // cin으로는 이렇게 하면됨
*/
#include <bits/stdc++.h>
using namespace std;
int n1, n2;
int main(){
    // 1안
    while(scanf("%d", &n1) != EOF){
        cout << 1 << '\n';
    }
    // 2안
    while(cin >> n2){
        cout << 1 << '\n';
    }
}