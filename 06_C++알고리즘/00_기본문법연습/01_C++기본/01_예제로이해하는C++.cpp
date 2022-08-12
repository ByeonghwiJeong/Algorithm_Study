#include <bits/stdc++.h>
// 표준 헤더 파일
// STL 라이브러리를 import 합니다.
// bits/stdc++.h 는 모든 표준 라이브러리가 포함된 헤더
// queue나 stack등을 사용할 때 #include<stack>입력할 필요X
using namespace std;
// "std라은 namespace를 사용한다"라는 뜻
//  cin, cout 사용시 std::cin std::cout가 아닌 cin, cout으로 사용 가능
// 네임 스페이스 같은 클래스 이름 구별, 모듈화에 쓰임
string a;
// <타입><변수명> 으로 선언
int main(){
	cin >> a; // 입력 : cin, scanf 
	cout << a << "\n"; // 출력 : cout, printf 
	return 0; 
	// 프로세스가 일이 정상적으로 마무리되며
    // process exit call
    // stdlib.h를 보면 
    // #define EXIT_SUCCESS 0
    // #define EXIT_FAILURE 1
    // 0을 return해야 프로세르를 성공적으로 종료
}
