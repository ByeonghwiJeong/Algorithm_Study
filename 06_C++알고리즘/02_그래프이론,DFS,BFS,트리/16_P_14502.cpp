/*
< 연구소 >
https://www.acmicpc.net/problem/14502
문제 
- N x M 직사각형
- 0:빈칸 / 1:벽 / 2:바이러스
- 벽3개를 세워야한다. 
입력
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
*/
#include<bits/stdc++.h>
using namespace std;
typedef pair<int, int> pi;
int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};
int n, m, a[10][10];
vector<pi> v;
bool vis[10][10];
void dfs(int r, int c){
    if(a[r][c] == 1 || vis[r][c]) return;
    vis[r][c] = 1;
    for(int i = 0; i < 4; i++){
        int nr = r + dr[i];
        int nc = c + dc[i];
        if(nr < 0 || nc < 0 || nr >= n || nc >= m){
            continue;
        }
        dfs(r + dr[i], c + dc[i]);
    }
}
int solve(){
    memset(vis, 0, sizeof(vis));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(a[i][j] == 2) dfs(i, j);
        }
    }
    int ans = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(!vis[i][j] && a[i][j] == 0) ans++;
        }
    }
    return ans;
}
int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
            if(!a[i][j]) v.push_back(pi(i, j));
        }
    }
    assert(v.size() >= 3);
    int ans = 0;
    for(int i = 0; i < v.size(); i++){
        for(int j = 0; j < i; j++){
            for(int k = 0; k < j; k++){
                a[v[i].first][v[i].second] = 1;
                a[v[j].first][v[j].second] = 1;
                a[v[k].first][v[k].second] = 1;
                ans = max(ans, solve());
                a[v[i].first][v[i].second] = 0;
                a[v[j].first][v[j].second] = 0;
                a[v[k].first][v[k].second] = 0;

            }
        }
    }
    cout << ans;
    return 0;
}
/*
짝짓기 >>> 스택
*/