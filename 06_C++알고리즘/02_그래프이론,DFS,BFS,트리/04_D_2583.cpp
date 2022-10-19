/*
< 영역구하기 >
https://www.acmicpc.net/problem/2583
문제
- 첫째줄 : M, N, K ~ [1\100]
    - (0, 0) ~ (N, M) 직사각형 영역
*/
#include<bits/stdc++.h>
using namespace std;
#define y1 aaaa
int a[104][104], m, n, k, x1, x2, y1, y2, visited[104][104];
const int dr[4] = {0, -1, 0, 1};
const int dc[4] = {-1, 0, 1, 0};
vector<int> ret;
int dfs(int r, int c){
    visited[r][c] = 1;
    int ret = 1;
    for(int i = 0; i < 4; i++){
        int nr = r + dr[i];
        int nc = c + dc[i];
        if(nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
        if(a[nr][nc] || visited[nr][nc]) continue;
        ret += dfs(nr, nc);
    }
    // cout << r << " : " << c << " : " << ret << "\n";
    return ret;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> m >> n >> k;
    for(int i = 0; i < k; i++){
        cin >> x1 >> y1 >> x2 >> y2;
        for(int x = x1; x < x2; x++){
            for(int y = y1; y < y2; y++){
                a[y][x] = 1;
            }
        }
    }
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(a[i][j] || visited[i][j]) continue;
            ret.push_back(dfs(i, j));
        }
    }
    sort(ret.begin(), ret.end());
    cout << ret.size() << "\n";
    for(int a : ret) cout << a << " ";
    return 0;
}
/*
< y1 재정의 > 
- y1을 사용하려면 
- #define y1 <임의의변수명>
< dfs함수 int형 >
- return int형태
< Connected Component의 크기 구하기 >
- return 형태로 더하기
- 전역변수로 cnt++;
< dfs 디버깅 - cout >
cout << r << " : " << c << " : " << ret << "\n";
*/
