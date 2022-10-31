/*
< 트리 >
https://www.acmicpc.net/problem/1068
문제 [ 트리 & 단방향그래프 ]
- 리프노드 :  자식 노드 0개
    0
  1    2
3   4
- 리프노드 2 3 4 : 3개
- 1번 지우는경우
0
   2
- 리프노드 2 : 1개
입력
1   : 노드의 개수 N ~ [1\50]
2   : 0번 ~ N-1번 노드에 대하여 부모노드의 번호
        - 부모노드가 없으면 -1
    - 부모노드번호v >>> i번노드
3   : 지울 노드 번호
---
5
-1 0 0 1 1
2
---
출력
1   : 입력으로 주어진 노드를 지웠을때 리프노드의 개수 
>> 2
*/
#include<bits/stdc++.h>
using namespace std;
int n, r, temp, root;
vector<int> adj[54];
int dfs(int here){
    int ret = 0;
    int child = 0;
    for(int there : adj[here]){
        if(there == r) continue;
        ret += dfs(there);
        child++;
    }
    if(child == 0) return 1;
    return ret;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> temp;
        if(temp == -1) root = i;
        else adj[temp].push_back(i);
    }
    cin >> r;
    if(r == root){
        cout << 0 << "\n";
        return 0;
    }
    cout << dfs(root) << "\n";
    return 0;
}
/*

*/
