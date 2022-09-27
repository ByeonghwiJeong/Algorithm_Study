#include <bits/stdc++.h>
using namespace std;
unordered_map<string, int> umap;
int main(){
    umap["bcd"] = 1;
    umap["aaa"] = 1;
    umap["aba"] = 1;
    for(auto i : umap){
        cout << i.first << " : " << i.second << "\n"; 
    }
    return 0;
}
/*
aba : 1
aaa : 1
bcd : 1
*/


