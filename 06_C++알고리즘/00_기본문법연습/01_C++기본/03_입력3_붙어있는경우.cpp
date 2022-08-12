/*
입력 방법 2 - scanf로 받기
-----
4 4
1000
0000
0111
0000
-----
%1d 와같이 앞에 1을 붙이면
한자리의 int만 받겠다는 뜻

문자를 받는경우는 다르다.
" %c"앞에 띄어쓰기를 붙임 
엔터도 문자로 취급하는것도 고려해야함
숫자인 d로 받으면 이런 현상 XX
----
LLMM
MMLL
----
*/
#include <bits/stdc++.h>
using namespace std;
int a[10][10], n, m;
char b[10][10];
int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%1d", &a[i][j]);
        }
    }
    // 문자를 받는 경우
    /*
    LLMM
    MMLL
    */
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 4; j++){
            scanf(" %c", &a[i][j]);
        }
    }
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 4; j++){
            cout << a[i][j];
        }
        cout << '\n';
    }
    /*
    76767777
    77777676
    */
    return 0;
}