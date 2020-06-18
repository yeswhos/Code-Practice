#include<iostream>
using namespace std;

void show(int& val) {
	val = 1000;
	cout << val << endl;
}

void show2(const int& val) {
	//val = 1000;
	cout << val << endl;
}

int main() {
	const int ref = 10;
	//ref = 1000;

	int a = 10;
	show2(a);
	show(a);
	system("pause");
	return 0;
}