#include<iostream>
using namespace std;

//ֵ����
void swap00(int a, int b) {
	int temp;
	temp = a;
	a = b;
	b = temp;
}

//��ַ����
void swap01(int* a, int* b) {
	int* temp;
	temp = a;
	a = b;
	b = temp;
}

//���ô���
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