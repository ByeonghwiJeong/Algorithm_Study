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
int n, a;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> a;
        int ret2 = 0, ret5 = 0;
        for(int j = 2; j <= a; j *= 2){
            ret2 += a / j;
        }
        for(int j = 5; j <= a; j *= 5){
            ret5 += a / j;
        }
        cout << min(ret2, ret5) << "\n";
    }
    return 0;
}
/*
구현 문제
*/
