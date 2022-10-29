/**//*
< 빈도정렬 >
https://www.acmicpc.net/problem/2910
문제
- 위대한 해커 창영이는 모든 암호를 깨는 방법을 발견
- 빈도를 조사
- 숫자N개로 이루어진 수열, 숫자는 모두C보다 작거나 같다.
- 이 숫자를 자주 등장하는 빈도순대로 정렬하려고한다.
- 등장빈도 같은 경우 먼저 나온순서
입력
- 첫째줄 : 메시지의 길이 N~[1\1000], 최대값 C~[1\1,000,000,000] 
- 둘째줄[N] : N개의 수

*/
#include<bits/stdc++.h>
using namespace std;
int n, c, a[1004];
vector<pair<int, int>> v;
map<int, int> mp, mp_first;
bool cmp(pair<int, int> a, pair<int, int> b){
    if(a.first == b.first){
        return mp_first[a.second] < mp_first[b.second];
        // mp_first:들어온순서
    }
    return a.first > b.first; // 갯수 내림차순
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> n >> c;
    for(int i = 0; i < n; i++){
        cin >> a[i];
        mp[a[i]]++;  // 숫자 갯수 Count
        if(mp_first[a[i]] == 0) mp_first[a[i]] = i + 1; 
        // 숫자 순서 check  : (i + 1)번째
    }
    for(auto it : mp){
        v.push_back({it.second, it.first});
    }
    sort(v.begin(), v.end(), cmp);;
    for(auto i : v){
        for(int j = 0; j < i.first; j++){
            cout << i.second << " ";
        }
    }
    return 0;
}
/*
- 구현 문제
- Custom operator 구현 - bool cmp
- Map에 참조만해도 0이 들어가는 성질을이용
if(mp_first[a[i]] == 0) mp_first[a[i]] = i + 1; 
*/
