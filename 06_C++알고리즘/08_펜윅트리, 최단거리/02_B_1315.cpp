#include <bits/stdc++.h>
using namespace std;
struct game{
    int x, y, c; 
};
vector<game> a;
int n, dp[1001][1001];
bool visited[101]; 

int rpg(int STR, int INT){
	int &ret = dp[STR][INT];
	if(ret != -1) return ret;

	ret = 0;
	int pnt = 0;
	vector<int> v;
	for(int i = 0; i < n; i++){
        if(a[i].x <= STR || a[i].y <= INT){
            ret++;
            if(!visited[i]){
                visited[i] = true;
                pnt += a[i].c;
                v.push_back(i);
            }
        }
	}

	for(int p = 0; p <= pnt; p++){
        int nextSTR = min(1000, STR + p);
        int nextINT = min(1000, INT + pnt - p);
        ret = max(ret, rpg(nextSTR, nextINT));
	}
	for(int here : v)
        visited[here] = false;

	return ret;
}

int main(){
	scanf("%d", &n);
	for(int i=0; i<n; i++){
        int STR, INT, PNT;
		scanf("%d %d %d", &STR, &INT, &PNT);
        a.push_back({STR, INT, PNT});
	}
	memset(dp, -1, sizeof(dp));
	printf("%d\n", rpg(1, 1));
}
