/*
< 팰린드롬 만들기 >
https://www.acmicpc.net/problem/1213
문제
- 이름이 주어졌을때 순서를 바꿔서 팰린드롬으로 만들어라
- 만들수 없을때 "I'm Sorry Hansoo"출력
- 정답 여러개 일때 사전순으로 정렬
*/
#include<bits/stdc++.h>
using namespace std;
string s, ret;
int cnt[200], flag;
char mid;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> s;
    for(char a : s) cnt[a]++;
    for(int i = 'Z'; i >= 'A'; i--){
        if(cnt[i]){
            if(cnt[i] % 2 == 1){
                mid = char(i);
                flag++;
                cnt[i]--;
            }
            if(flag == 2) break;
            for(int j = 0; j < cnt[i]; j += 2){
                ret = char(i) + ret + char(i);
            }
        }
    }
    if(mid) ret.insert(ret.begin() + ret.size() / 2, mid);
    if(flag == 2) cout << "I'm Sorry Hansoo\n";
    else cout << ret << "\n";
    return 0;
}
/*
- Counting Array : cnt[200]
    - 모든 알파벳 저장
- 홀수 2개 이상인경우 불가능 
    - flag로 홀수 갯수 Counting
- cnt[i] 홀수 확인법
    - cnt[i] % 2 == 1
    - cnt[i] & 1
*/