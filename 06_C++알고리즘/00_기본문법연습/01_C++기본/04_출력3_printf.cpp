/*
str.c_str() >>  사용
*/
#include <bits/stdc++.h>
using namespace std;
int a = 1;
char s = 'a';
string str = "Avengers";
double b = 1.223123;

int main(){
    printf("I'm a iron man : %d\n",a);
    printf("I'm a iron man : %c\n",s);
    printf("I'm a iron man : %s\n",str.c_str());
    printf("I'm a iron man : %lf\n",b);
    return 0;
}
/*
I'm a iron man : 1
I'm a iron man: a
I'm a iron man: Avengers
I'm a iron man : 1.223123
*/