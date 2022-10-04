/*
< 트럭 주차 >
https://www.acmicpc.net/problem/2979
문제
- 트럭이 3대 있다. 주차비용???
- 한 대 : 1분에 한대당 A원
- 두 대 : 1분에 한대당 B원
- 세 대 : 1분에 한대당 C원
- A, B, C가 주어지고, 트럭이 추차된 시간이 주어졌을때 얼마?
*/
#include<bits/stdc++.h>
using namespace std;
int t[101], A, B, C, s, e, ret; // 전역변수로 해야 0으로 초기화됨
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> A >> B >> C;
    for(int i = 0; i < 3; i++){
        cin >> s >> e;
        for(int i = s; i < e; i++){
            t[i]++;
        }
    }
    for(int i = 1; i <= 100; i++){
        if(t[i]){
            if(t[i] == 1) ret += A;
            else if(t[i] == 2) ret += B * 2;
            else if(t[i] == 3) ret += C * 3;
        }
    }
    cout << ret << "\n"; 
    return 0;
}
/*
트럭이 주차장에 
도착시각과 떠나는시각의 전후 관계를 
확실히 해야한다!!!
문제 조건)
- 도착한 시간은 항상 떠난 시간보다 앞선다.
*/