/*
< 기상캐스터 >
https://www.acmicpc.net/problem/10709
문제 
- 세로(남북) H x 가로(동서) W ~ [1 \ 100]
- 위(북)부터 i번째, 왼쪽(서)에서 j번째 ~ (i, j)
입력
3 4
c..c
..c.
....
출력
0 1 2 0
-1 -1 0 1
-1 -1 -1 -1
*/
#include<bits/stdc++.h>
using namespace std;
int r, c, a[104][104];
string s;
int main(){
    cin >> r >> c;
    for(int i = 0; i < r; i++){
        cin >> s;
        for(int j = 0; j < c; j++){
            if(s[j] == '.') a[i][j] = -1;
            else a[i][j] = 0;
        }
    }
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            if(a[i][j] == 0){
                int cnt = 1;
                while(a[i][j + 1] == -1){
                    a[i][j + 1] = cnt++;
                    j++;
                }
            }
        }
    }
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++) cout << a[i][j] << " ";
        cout << "\n";
    }
    return 0;
}
/*
구현 문제
*/
