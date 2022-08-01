#include <bits/stdc++.h>
using namespace std;
int ret_a = 1;
void a(){
	ret_a = 2;
	cout << ret_a << "\n";
	return;
}
double b(){
	return 1.233;
}
int main(){
	a();
	double ret_b = b();
	char a = 'a';
	string b = "wow fantastic";
	string c = "wow";
	c += " ";
	c += "fantastic";
	cout << ret_b << "\n";
	cout << a << "\n";
	cout << b << "\n";
	cout << c << "\n";
	cout << c.size() << "\n";	
	return 0;
}
// a라는 함수가 ret을 바꾸고 
// 리턴 X >>> void 사용
// return 하는 값의 타입에 맞추어서
// void, string, double, int, bool ... 선택 
