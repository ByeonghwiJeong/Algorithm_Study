/*
< 보물섬 >
https://www.acmicpc.net/problem/2589
문제 [ bfs - 최단경로 ]
- 직사각형모양
- 육지(L) or 바다(W)
- 한칸 이동시 한시간걸림 : 상하좌우 이웃한 육지만 이동
- 보물은 서로간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두곳에 나뉘어 묻혀있다.
입력)
1   : 세로크기, 가로크기 ~ [1 \ 50]
출력)
1   : 두 곳 사이를 최단 거리로 이동하는 시간을 출력
*/
#include<bits/stdc++.h>
using namespace std;
int n, m, mx, visited[54][54];
const int dr[] = {0, 1, 0, -1};
const int dc[] = {1, 0, -1, 0};
char a[54][54];
void bfs(int r, int c){
    memset(visited, 0, sizeof(visited));
    visited[r][c] = 1;
    queue<pair<int, int>> q;
    q.push({r, c});
    while(q.size()){
        tie(r, c) = q.front(); q.pop();
        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
            if(visited[nr][nc]) continue;
            if(a[nr][nc] == 'W') continue;
            visited[nr][nc] = visited[r][c] + 1;
            q.push({nr, nc});
            mx = max(mx, visited[nr][nc]);
        }
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
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(a[i][j] == 'L') bfs(i, j);
        }
    }
    cout << mx - 1 << "\n";
    return 0;
}
/*

*/
