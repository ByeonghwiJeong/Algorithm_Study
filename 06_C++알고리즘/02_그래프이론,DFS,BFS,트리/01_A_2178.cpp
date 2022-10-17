/*
< 미로 탐색 >
https://www.acmicpc.net/problem/2178
문제
- N x M 배열에서 1:이동가능 / 0:이동불가
- (1, 1)에서 출발하여 (N, M)의 위치로 이동
- 지나야하는 최소 칸수
- N, M ~ [2 \ 100]
입력
4 6
101111
101010
101011
111011
출력
15
*/
#include<bits/stdc++.h>
using namespace std;
const int max_n = 104;
int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};
int n, m, a[max_n][max_n], visited[max_n][max_n], r, c;
int main(){
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%1d", &a[i][j]);
        }
    }
    queue<pair<int, int>> q;
    visited[0][0] = 1;
    q.push({0, 0});
    while(q.size()){
        tie(r, c) = q.front(); q.pop();
        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr < 0 || nr >= n || nc < 0 || nc >= m || a[nr][nc] == 0) continue;
            if(visited[nr][nc]) continue;
            visited[nr][nc] = visited[r][c] + 1;
            q.push({nr, nc});
        }
    }
    printf("%d", visited[n - 1][m - 1]);
    return 0;
}
/*
< 따닥 따닥 붙어있는것 받기 >
1. string 으로 변환
cin >> n >> m;
for(int j=0; j < n; j++){
    cin >> s;
}
2. scanf로 받기
scanf("%1d", &a[i][j]);

조건 순서 중요!!
if(nr < 0 || nr >= n || nc < 0 || nc >= m || a[nr][nc] == 0) 
*/