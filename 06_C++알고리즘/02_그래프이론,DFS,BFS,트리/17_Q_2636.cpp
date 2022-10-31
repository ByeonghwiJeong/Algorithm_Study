/*
< 치즈 >
https://www.acmicpc.net/problem/2636
문제 
- 세로n 가로m 최대길이 100 사격형판
- 0:판 / 1:치즈 
- 1시간마다 가장자리부터 녹음
- 다녹기 1시간 직전의 1의 갯수
입력
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
출력
3 - 모두녹는시간
5 - 모두녹기 한 시간 전에 남아있는 치즈 조각
*/
#include<bits/stdc++.h>
using namespace std;
int a[104][104], visited[104][104];
int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};
int n, m, cnt, cnt2;
vector<pair<int, int>> v;
void dfs(int r, int c){
    visited[r][c] = 1;
    if(a[r][c] == 1){
        v.push_back({r, c});
        return;
    }
    for(int i = 0; i < 4; i++){
        int nr = r + dr[i];
        int nc = c + dc[i];
        if(nr < 0 || nc < 0 || nr >=  n || nc >= m || visited[nr][nc]){
            continue;
        }
        dfs(nr, nc);
    }
    return;
}
int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    while(true){
        cnt2 = 0;
        fill(&visited[0][0], &visited[0][0] + 104 * 104, 0);
        v.clear();
        dfs(0, 0);
        for(pair<int, int> b : v){
            cnt2++;
            a[b.first][b.second] = 0;
        }
        bool flag = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(a[i][j] != 0) flag = 1;
            }
        }
        cnt++;
        if(!flag) break;
    }
    cout << cnt << "\n" << cnt2 << "\n";
    return 0;

}
/*
짝짓기 >>> 스택
*/
