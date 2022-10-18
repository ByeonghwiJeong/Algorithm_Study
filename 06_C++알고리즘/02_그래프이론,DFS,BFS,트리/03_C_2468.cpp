/*
< 안전영역 >
https://www.acmicpc.net/problem/2468
문제
- N x N 행렬에 높이정보가 입력된다. 높이 - [1\100]
- 높이 기준(d)을 잡아서 d보다 큰 connected component의 개수
*/
#include<bits/stdc++.h>
using namespace std;
int a[101][101], e[101][101], visited[101][101], n, temp, ret = 1;
int dr[4] = {0, 1, 0, -1}, dc[4] = {1, 0, -1, 0};
void dfs(int r, int c, int d){
    // visited[r][c] = 1;
    for(int i = 0; i < 4; i++){
        int nr = r + dr[i];
        int nc = c + dc[i];
        if(nr < 0 || nc < 0 || nr >= n || nc >= n) continue;
        if(visited[nr][nc] || a[nr][nc] <= d) continue;
        visited[nr][nc] = 1;
        dfs(nr, nc, d);
    }
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> a[i][j];
        }
    }
    for(int d = 1; d < 101; d++){
        fill(&visited[0][0], &visited[0][0] + 101 * 101, 0);
        int cnt = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(visited[i][j] || a[i][j] <= d) continue;
                visited[i][j] = 1;
                dfs(i, j, d);
                cnt++;
            }
        }
        ret = max(ret, cnt);
    }
    cout << ret << "\n";
    return 0;
}
/*

*/
