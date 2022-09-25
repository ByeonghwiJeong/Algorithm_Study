#include <bits/stdc++.h>
using namespace std;
int n, m, a[10][10];
string s;
int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> s;
        for(int j = 0; j < m; j++){
            a[i][j] = s[j] - '0';
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j];
        }
        cout << '\n';
    }
    return 0;
}
/*
4 4
1000
0000
0111
0000
----
1000
0000
0111
0000
*/

