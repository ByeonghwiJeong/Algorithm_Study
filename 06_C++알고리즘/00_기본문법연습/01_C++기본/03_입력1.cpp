/*
보통 cin과 scanf로 받습니다.
"%d"는 정수형으로 받겠다는 뜻
- %lf : 실수형
- %c : char형
- %s : string
- %ld : long long형

문제에서 형식을 기반으로 입력이 주어지지 않는경우 
cin이 좋다.
- cin은 개행문자(띄어쓰기, 엔터)를 구분하여 입력을 받습니다.

예) 3.22와 같이 입력 형식이 주어졌을때 scanf사용
---> scanf("%d.%d", &m1, &m2);
>>> But 실수형 연산은 정신건강에 좋지않음
>>> 정수형으로변환해서 사용

*/
#include <bits/stdc++.h>
using namespace std;
int a;
int main(){
    cin >> a;
    scanf("%d", &a);
    return 0;
}