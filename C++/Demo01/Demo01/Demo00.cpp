#include<iostream>
using namespace std;

int main() {
	int a = 10;
	int * p;
	p = &a;
	cout << "a�ĵ�ַΪ: " << &a << endl;
	cout << "p��Ϊ" << p << endl;
	cout << "p = " << *p << endl;
	system("pause");
	return 0;
}