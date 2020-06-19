#include<iostream>
using namespace std;

void func(int a, int) {
	cout << "func" << endl;
}

int main() {
	func(10, 10);
	system("pause");
	return 0;
}