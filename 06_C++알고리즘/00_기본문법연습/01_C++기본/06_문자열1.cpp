/*
- reverse
������ ���ڿ��� �ٲ�����ϴ�
begin�� end�� ���� ��ü�� �ٲ㵵 �ǰ�
dopa.begin(), dopa.begin() + 3 �̷������� �κи� �ٲ���� ���� �ֽ��ϴ�.

- substr
�����������κ��� ��� ���ڿ��� �̾Ƴ��ϴ�.
(��������, �) �̷��� 2���� �Ű������� ���� �˴ϴ�. 
���� ���������� �ְ� �Ǹ� ���������� ���ڿ��� �̾Ƴ��ϴ�.

- find
��� ���ڿ��� ����ֳ� ã���ϴ�. 
���� ã�� ���Ѵٸ� ���ڿ��� �� ��ġ�� string::npos�� ��ȯ
*/
#include <bits/stdc++.h>
using namespace std;
string dopa = "amumu is best";
int main(){
    cout << dopa << "\n";
    // amumu is best
    if(dopa.find("amumu") != string::npos){
        cout << "amumu in dopa!\n";
    }
    // amumu in dopa!
    cout << dopa.substr(0, 3) << "\n";
    // amu
    reverse(dopa.begin(), dopa.end());
    cout << dopa << "\n";
    // tseb si umuma
    return 0;
}