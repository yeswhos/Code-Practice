#include<iostream>
using namespace std;

int& show00() {
	int a = 10;
	return a;
}

int& show01() {
	static int a = 20;
	return a;
}

int main() {
	int& ref = show00();
	cout << ref << endl;
	cout << ref << endl;

	int& ref2 = show01();
	cout << ref2 << endl; 
	cout << ref2<< endl;

	show01() = 1000;
	cout << show01() << endl;
	cout << show01() << endl;

	system("pause");
	return 0;
}
