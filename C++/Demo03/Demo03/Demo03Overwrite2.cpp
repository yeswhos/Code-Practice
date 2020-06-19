#include<iostream>
using namespace std;

void func(int& a) {
	cout << "func int & a" << endl;
}

void func(const int& a) {
	cout << "func const int & a" << endl;
}

void func1(int a, int b = 10) {
	cout << "func int b = 10" << endl;
}

void func2(int a, int b) {
	cout << "func int b" << endl;
}

int main() {
	int a = 10;
	func(a);
	const int b = 20;
	func(b);
	system("pause");
	return 0;
}