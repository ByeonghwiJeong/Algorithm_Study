/*
< 치킨 배달 >
https://www.acmicpc.net/problem/15686
문제 [ 스택 - 짝짓기문제 ]
- N x N 도시 
- 도시의 각칸은 빈칸:0 , 집:1, 치킨집:2 중하나
- 도시의 칸은 (r, c)와 같은 형태 : r,c는 1부터시작
- 각각의 집은 치킨거리가 있다. 
- 임의의 두칸 (r1, c1) ~ (r2, c2)의 거리는 |r1-r2| + |c1-c2|
- 치킨집을 폐업시키려고한다. 
- 이도시에서 가장 수익을 많이 낼수 있는 치킨집의 수 : 최대 M
- 도시에 있는 치킨집중에서 최대 M개를 고르고 나머지 치킨집 폐업
- 어떻게 고르면 [도시의 치킨 거리]가 가장 작게 될지 구하라
입력)
1   : N~[2\50], M~[1\13]
2   : N x N의 0 1 2 
    - 집의 개수는 2N개를 넘지않으며 적어도 1개는 존대
    - 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
출력)
1   : 폐업시키지 않을 치킨집을 최대 M개 골랐을 때, 도시의 치킨거리의 최솟값?
*/
#include<bits/stdc++.h>
using namespace std;
int n, m, a[54][54], result = 987654321;
vector<vector<int>> chickenList;
vector<pair<int, int>> _home, chicken;
void combi(int start, vector<int> v){
    if(v.size() == m){
        chickenList.push_back(v);
        return;
    }
    for(int i = start + 1; i < chicken.size(); i++){
        v.push_back(i);
        combi(i, v);
        v.pop_back();
    }
    return;
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> a[i][j];
            if(a[i][j] == 1) _home.push_back({i, j});
            if(a[i][j] == 2) chicken.push_back({i, j});
        }
    }
    vector<int> v;
    combi(-1, v);
    for(vector<int> cList : chickenList){
        int ret = 0;
        for(pair<int, int> home : _home){
            int _min = 987654321;
            for(int ch : cList){
                int _dist = abs(home.first - chicken[ch].first) + abs(home.second - chicken[ch].second);
                _min = min(_min, _dist);
            }
            ret += _min;
        }
        result = min(result, ret);
    }
    cout << result << "\n";
    return 0;
}