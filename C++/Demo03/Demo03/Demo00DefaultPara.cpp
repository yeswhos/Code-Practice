#include<iostream>
using namespace std;

int func(int a, int b = 20, int c = 30) {
	return a + b + c;
}

int main() {
	cout << func(10, 200) << endl;
	system("pause");
	return 0;
}