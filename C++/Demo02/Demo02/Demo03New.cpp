#include<iostream>
using namespace std;

int* func() {
	int* p = new int(10);
	return p;
}

void test() {
	int *p = func();
	cout << p << endl;
	delete p;
}

int * test_new() {
	int* arr = new int[10];
	for (int i = 0; i < 10; i++) {
		arr[i] = i + 100;
	}
	for (int i = 0; i < 10; i++) {
		cout << arr[i] << endl;
	}
	return arr;
}
int main() {
	test();
	int *arr = test_new();
	for (int i = 0; i < 10; i++) {
		cout << arr[i] << endl;
	}
	//test_new();
	system("pause");
	return 0;
}