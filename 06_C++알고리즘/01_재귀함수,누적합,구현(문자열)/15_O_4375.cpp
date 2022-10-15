/*
< 곱셈 >
https://www.acmicpc.net/problem/4375
문제
- 2와 5로 나누어 떨어지지 않는 정수 n (1 ≤ n ≤ 10000)
- 1로만 이루어진 n의 배수를 찾는 프로그램을 작성
*/
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
int main(){
    while(scanf("%d", &n) != EOF){
        int cnt = 1, ret = 1;
        while(true){
            if(cnt % n == 0){
                printf("%d\n", ret);
                break;
            }else{
                cnt = (cnt * 10) + 1;
                cnt %= n;
                ret++;
            }
        }
    }
    return 0;
}
/*
21억이하의 자연수 >>> long long자료형
재귀함수 :  기저사례체크!! ~ b==1 경우
*/
