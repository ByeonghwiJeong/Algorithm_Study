/*
< 영역구하기 >
https://www.acmicpc.net/problem/1992
문제
- 흑백영상 압축하여 표현하는 데이터구조 : 쿼드 트리(Quad Tree)
- 흰점-0, 검은점-1
<쿼드트리>
- 주어진영상이 모두 0으로만 되어 있으면 압축결과는 "0"
- 01이 섞여 있으면 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래
입력
- 첫째줄 : N ~ 2의 제곱수 [1 \ 64] 
- 둘째줄 : N의 문자열 N개 들어온다.
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
출력
((110(0101))(0010)1(0001))
*/
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
string s;
char a[101][101]; // 문자 char으로 형 선언
string quard(int r, int c, int size){
    if(size == 1) return string(1, a[r][c]);
    char b = a[r][c];
    string ret = "";
    int half_size = size / 2;
    for(int i = r; i < r + size; i++){
        for(int j = c; j < c + size; j++){
            if(b != a[i][j]){
                ret += '(';
                ret += quard(r, c, half_size);
                ret += quard(r, c + half_size, half_size);
                ret += quard(r + half_size, c, half_size);
                ret += quard(r + half_size, c + half_size, half_size);
                ret += ')';
                return ret;
            }
        }
    }
    return string(1, b);
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> s;
        for(int j = 0; j < n; j++){
            a[i][j] = s[j];
        }
    }
    cout << quard(0, 0, n) << "\n";
    return 0;
}
/*
string(1, a[r][c])
- https://cplusplus.com/reference/string/string/string/
- string(size_t n, char c)
n : c의 개수
c : 문자열에 채우고 싶은 문자
*/
