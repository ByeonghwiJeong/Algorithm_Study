#include <iostream>
#include <string>

using namespace std;

int main(){
    cout << "Hell world !" << endl;
    cout << "Please input your name" << endl;
    string str_name;
    getline (cin, str_name);
    cout << "Name: " << str_name << endl;
    return 0;
}