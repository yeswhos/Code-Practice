#include<iostream>
using namespace std;

void func() {
	cout << "func kong" << endl;
}

void func(int a) {
	cout << "func int" << endl;
}

void func(double a) {
	cout << "func double" << endl;
}

void func(int a, double b) {
	cout << "func int double" << endl;
}

void func(double b, int a) {
	cout << "func double int" << endl;
}

int main() {
	func();
	func(10);
	func(3.14);
	func(10, 3.14);
	func(3.14, 10);
	system("pause");
	return 0;
}