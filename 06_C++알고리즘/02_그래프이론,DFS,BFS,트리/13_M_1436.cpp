/*
< 영화감독 슘 >
https://www.acmicpc.net/problem/1436
문제 
- 종말수 어떤수에 666이 적어도 3개이상 연속으로 들어가는 수
입력
숫자 N ~ [1 \ 10,000)
출력
*/
#include<bits/stdc++.h>
using namespace std;
int n;
int main(){
    cin >> n;
    int i = 666;
    for(;; i++){
        if(to_string(i).find("666") != string::npos) n--;
        if(n == 0) break;
    }
    cout << i << "\n";
    return 0;
}
/*
구현 문제
*/
