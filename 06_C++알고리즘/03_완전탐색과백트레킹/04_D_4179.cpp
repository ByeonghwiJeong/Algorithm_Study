#include <bits/stdc++.h>
using namespace std;
const int INF = 987654321;
char a[1001][1001];
int n, m, sr, sc, r, c, ret;
int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};
int fire_check[1001][1001], person_check[1001][1001];
bool in(int a, int b){
    return 0 <= a && a < n && 0 <= b && b < m;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    queue<pair<int, int>> q;
    cin >> n >> m;
    fill(&fire_check[0][0], &fire_check[0][0] + 1001 * 1001, INF);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
            if(a[i][j] == 'F'){
                fire_check[i][j] = 1;
                q.push({i, j});
            }else if(a[i][j] == 'J'){
                sr = i;
                sc = j;
            }
        }
    }

    while(q.size()){
        tie(r, c) = q.front();
        q.pop();
        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(!in(nr, nc)) continue;
            if(fire_check[nr][nc] != INF) continue;
            if(a[nr][nc] == '#') continue;
            fire_check[nr][nc] = fire_check[r][c] + 1;
            q.push({nr, nc});
        }
    }

    person_check[sr][sc] = 1;
    q.push({sr, sc});
    while(q.size()){
        int r = q.front().first;
        int c = q.front().second;
        q.pop();
        if(r == 0 || r == n - 1 || c == 0 || c == m - 1){
            ret = person_check[r][c];
            break;
        }
        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(!in(nr, nc)) continue;
            if(person_check[nr][nc] != 0) continue;
            if(a[nr][nc] == '#') continue;
            if(person_check[r][c] + 1 >= fire_check[nr][nc]) continue;
            person_check[nr][nc] = person_check[r][c] + 1;
            q.push({nr, nc});
        }
    }
    if(ret == 0) cout << "IMPOSSIBLE";
    else cout << ret;
    return 0;
}
