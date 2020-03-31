#include<iostream>
using namespace std;

int addMethod(int a, int b) {
	int c = a + b;
	return c;
}

int main() {
	int c = addMethod(2, 3);
	cout << c << endl;
	system("pause");
	return 0;
}