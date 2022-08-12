/*
<< split >>

C++에서는 split함수가 지원하지않음
문자열을 문자열 기준으로 나누는 split함수 구현
*/
#include <bits/stdc++.h>
using namespace std;

vector<string> split(string input, string deplimiter){
    vector<string> ret;
    long long pos = 0;
    string token = "";
    while((pos = input.find(delimiter)) != string::npos){
        token = input.substr(0, pos);
        ret.push_back(token);
        input.erase(0, pos + deplimiter.length());
    }
    ret.push_back(input);
    return ret;
}

vector<string> split_debug(string input, string delimiter){
    vector<string> ret;
    long long pos = 0;
    while((pos = input.find(delimiter)) != string::npos){
        long long pos = input.find(delimiter);
        cout << "POS : "
    }
}
