/*
< 유기농 배추 >
https://www.acmicpc.net/problem/1012
문제
- 테스트케이스 & N*M행렬의 1값 Connected 컴포넌트 갯수
*/
#include<bits/stdc++.h>
using namespace std;
int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};
int m, n, k, r, c, ret, nr, nc, t;
int a[51][51];
bool visited[51][51];
void dfs(int r, int c){
	visited[r][c] = 1;
    for(int i = 0; i < 4; i++){
        nr = r + dr[i];
        nc = c + dc[i];
        if(nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
        if(a[nr][nc] == 0 || visited[nr][nc]) continue;
        // visited[nr][nc] = 1;  
        dfs(nr, nc);
    }
    return;
}

int main(){
    // ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> t;
    while(t--){
        fill(&a[0][0], &a[0][0] + 51 * 51, 0);
        fill(&visited[0][0], &visited[0][0] + 51 * 51, 0);
        ret = 0;
        cin >> m >> n >> k;
        for(int i = 0; i < k; i++){
            cin >> c >> r;
            a[r][c] = 1;
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(a[i][j] == 0 || visited[i][j]) continue;
                // visited[i][j] = 1;
                dfs(i, j);
                ret++;
            }
        }
        cout << ret << "\n";
    }
    return 0;
}
/*
< 테스트 케이스 >
- 테스트 케이스 마다 초기화 중요!!!
- int a[][], bool visited[][], int ret
fill(&visited[0][0], &visited[0][0] + 51 * 51, 0);
< 방문체크 위치 >
1. dfs함수 처음 1번
2. 함수호출전 방문체크후 첫번째 & 함수내주에서 방문체크후 두번째
*/
