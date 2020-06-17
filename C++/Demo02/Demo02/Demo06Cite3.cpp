#include<iostream>
using namespace std;

//值传递
void swap00(int a, int b) {
	int temp;
	temp = a;
	a = b;
	b = temp;
}

//地址传递
void swap01(int* a, int* b) {
	int* temp;
	temp = a;
	a = b;
	b = temp;
}

//引用传递
void swap02(int& a, int& b) {
	int temp;
	temp = a;
	a = b;
	b = temp;
}
int main() {
	int a = 10;
	int b = 20;
	//swap00(a, b);
	//swap01(&a, &b);
	swap02(a, b);
	cout << a << endl;
	cout << b << endl;
	system("pause");
	return 0;
}