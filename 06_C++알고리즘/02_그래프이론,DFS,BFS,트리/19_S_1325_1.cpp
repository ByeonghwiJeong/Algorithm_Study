/*
< 트리 >
https://www.acmicpc.net/problem/1325
문제 [  ]
- N개의 컴퓨터
- 한번의 해킹으로 여러개의 컴퓨터를 하려함
- A가 B를 신뢰하는경우 B를 해킹하면 A도 해킹
- 입력으로 신뢰하는관계가 주어짐
입력
1   : N~[1 \ 10,000], M~[1 \ 100,000]
2-M : M개의 줄에 신뢰관계가 주어짐
      - A B
      - A가 B를 신뢰한다.
      - B >>> A [ 단방향 그래프 ]
출력
- 한번에 가장 많은 컴퓨터를 해킬할 수 있는 컴퓨터의 번호를 오름차순으로 출력

*/
#include<bits/stdc++.h>
using namespace std;

vector<int> v[10001];
int dp[10001], mx, visited[10001], n, m, a, b;

int dfs(int here){
    visited[here] = 1;
    int ret = 1;
    for(int there : v[here]){
        if(visited[there]) continue;
        ret += dfs(there);
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> n >> m;
    while(m--){
        cin >> a >> b;
        v[b].push_back(a);
    }
    for(int i = 1; i <= n; i++){
        memset(visited, 0, sizeof(visited));
        dp[i] = dfs(i);
        mx = max(dp[i], mx);
    }
    for(int i = 1; i <= n; i++) if(mx == dp[i]) cout << i << " ";
    return 0;
}
/*

*/
