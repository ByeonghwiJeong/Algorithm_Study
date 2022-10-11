/*
< 나는야 포켓몬 마스터 이다솜 >
https://www.acmicpc.net/problem/1620
문제
- 첫번째 줄 : 두 개의 정수 N, M ~ [1 \ 100,000]
    - N : 포켓몬의 개수 N
    - M : 내가 맞춰야 하는 문제의 개수 M
- 두번째 줄[N] : N개의 줄에 1 ~ N번 포켓몬 영어이름
- 세번째 줄[M] : M개의 줄에 내가 맞춰야하는 문제
- 출력 번호 > 이름 \ 이름 > 번호
*/
#include<bits/stdc++.h>
using namespace std;
int n, m;
string s;
map<string, int> mp;
map<int, string> mp2;
string a[100004];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> s;
        mp[s] = i + 1;
        mp2[i + 1] = s;
        a[i + 1] = s;
    }
    for(int i = 0; i < m; i++){
        cin >> s;
        if(atoi(s.c_str()) == 0){
            cout << mp[s] << "\n";
        }else{
            cout << a[atoi(s.c_str())] << "\n";
            //cout << mp2[atoi(s.c_str())] << "\n";
        }
    }
    return 0;
}
/*
- str ➡️ int
    - Map - O(logN) check
    - Arr - O(N)
- int ➡️ str
    - Map - O(logN)
    - Arr - O(1) check
- atoi(s.c_str())
    - 숫자(1)인지 문자(0)인지 판별
    - 0은 체크못함 - 따로 로직구현
    - PYTHON : s.isdigit()
*/