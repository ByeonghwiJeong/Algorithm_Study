/*
< 곱셈 >
https://www.acmicpc.net/problem/1629
문제
- A를 B번 곱한수를 C로 나눈 나머지
*/
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll a, b, c;
ll go(ll a, ll b){
    if(b == 1) return a % c;
    ll ret = go(a, b / 2);
    ret = (ret * ret) % c;
    if(b % 2) ret = (ret * a) % c;
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> a >> b >> c;
    cout << go(a, b) << "\n";
    return 0;
}
/*
21억이하의 자연수 >>> long long자료형
재귀함수 :  기저사례체크!! ~ b==1경우
*/
