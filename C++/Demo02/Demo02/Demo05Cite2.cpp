#include<iostream>
using namespace std;

int main() {
	int a = 10;
	int c = 20;
	//int& b;
	int& b = a;
	cout << a << endl;
	cout << b << endl;
	b = 20;
	//传递值不是地址
	b = c;
	cout << a << endl;
	cout << b << endl;
	system("pause");
	return 0;
}