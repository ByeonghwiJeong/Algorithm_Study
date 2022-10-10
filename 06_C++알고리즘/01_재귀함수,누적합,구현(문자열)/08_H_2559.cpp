/*
< 수열 >
https://www.acmicpc.net/problem/2559
문제
- 첫번째 줄 : 두 개의 정수 N, K
    - N : 온도를 측정한 전체 날짜의 수
    - K : 합을 구하기 위한 연속적인 날짜의 수
- 두번째 줄 : N개의 매일 측정한 온도 [-100 \ 100]
*/
#include<bits/stdc++.h>
using namespace std;
int n, k, temp, psum[100001], ret = -1000000;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> k;
    for(int i = 1; i <= n; i++){
        cin >> temp;
        psum[i] = psum[i - 1] + temp;
    }
    for(int i = k; i <= n; i++){
        ret = max(ret, psum[i] - psum[i - k]);
    }
    cout << ret << "\n";
    return 0;
}
/*
- 전형적인 누적합문제
*/