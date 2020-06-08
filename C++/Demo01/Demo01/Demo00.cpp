#include<iostream>
using namespace std;

int main() {
	int a = 10;
	int * p;
	p = &a;
	cout << "a的地址为: " << &a << endl;
	cout << "p的为" << p << endl;
	cout << "p = " << *p << endl;
	system("pause");
	return 0;
}