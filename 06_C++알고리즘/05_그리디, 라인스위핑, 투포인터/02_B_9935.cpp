#include<bits/stdc++.h>
using namespace std;
string S, T, ret;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    for(char a : S){
        ret += a;
        if (ret.size() < T.size()) continue;
        if (ret.substr(ret.size() - T.size()) == T) ret.erase(ret.size() - T.size());
    }
    if (ret.empty()) cout << "FRULA" << '\n';
    else cout << ret << '\n';
    return 0;
}