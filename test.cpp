#include <bits/stdc++.h>

using namespace std;

vector<string> split(string input, string delimiter){
    vector<string> ret;
    long long pos = 0;
    string token = "";
    while ((pos = input.find(delimiter)) != string::npos){
        token = input.substr(0, pos);
        ret.push_back(token);
        input.erase(0, pos + delimiter.length());
    }
    ret.push_back(input);
    return ret;
}

vector<string> split_debug(string input, string delimiter){
    vector<string> ret;
    long long pos = 0;
    string token = "";
    while ((pos = input.find(delimiter)) != string::npos){
        long long pos = input.find(delimiter);
        cout << "POS : " << pos << "\n"; // 15 12 15 15
        if(pos == string::npos) break;
        token = input.substr(0, pos);
        ret.push_back(token);
        input.erase(0, pos + delimiter.length());
    }
    ret.push_back(input);
    return ret;
}

int main(){
    string s = "안녕하세요 큰돌은 천재입니다! 정말이에요!";
    string d = " ";
    vector<string> a = split(s, d);
    string s2 = "aaaa bbb ccccc ee dddddddd!";
    vector<string> c = split_debug(s2, d);
    // 4 3 5 2 띄어쓰기를 찾아 해당 첫번째 인덱스를 반환한다.
    // 문자열이 erase되기 때문에 aaaa, bb 이런식으로 되는것도 생각
    for(string b : a) cout << b << "\n";
}
/*
POS : 4
POS : 3
POS : 5
POS : 2
안녕하세요
병휘는
천재입니다!
정말이에요!
*/
