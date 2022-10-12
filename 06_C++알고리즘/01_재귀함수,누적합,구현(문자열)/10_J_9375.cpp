/*
< 패션왕 신해빈 >
https://www.acmicpc.net/problem/9375
문제
- 해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 입지않는다.
- 예) 오늘 - 안경, 코드, 상의, 신발
      내일 - 바지를 추가로 입거나 안경대신 렌즈를 착용해야한다.
- 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
입력
- 첫째줄 : 테스트 케이스 수
- 각테스트 : 의상의 수 n ~ [0 \ 30], n개의 의상이름 + 의상종류
*/
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int t, n;
string a, b;
int main(){
    cin >> t;
    while(t--){
        map<string, int> _map;
        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> a >> b;
            _map[b]++;
        }
        ll ret = 1;
        for(auto c : _map){
            ret *= ((ll)c.second + 1);
        }
        ret--;
        cout << ret << "\n";
    }
    return 0;
}
/*
자료구조 : map<string, int>
- 상품의 이름은 빼고 종류만 카운팅한다
map for문 
- for(auto c : _map) ret *= (ll)c.second + 1
경우의 수 결과값은 매우 커질 수 있다.
- long long 형으로 default 출력하자!!!
*/