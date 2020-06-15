#include<iostream>
using namespace std;

int g_a = 10;
int g_b = 10;

//全局常量
const int c_g_a = 10;
const int c_g_b = 10;

int main() {
	int a = 10;
	int b = 10;

	cout << "Local Variable a is " << (int)&a << endl;
	cout << "Local Variable b is " << (int)&b << endl;

	cout << "Global Variable a is " << (int)&g_a << endl;
	cout << "Global Variable b is " << (int)&g_b << endl;

	static int s_a = 10;
	static int s_b = 10;
	cout << "Static Variable a is " << (int)&s_a << endl;
	cout << "Static Variable b is " << (int)&s_b << endl;

	cout << "String constant is " << (int)&"Hello World" << endl;

	cout << "Global constant a is " << (int)&c_g_a << endl;
	cout << "Global constant b is " << (int)&c_g_b << endl;

	const int c_l_a = 10;
	const int c_l_b = 10;

	cout << "Local constant a is " << (int)&c_l_a << endl;
	cout << "Local constant b is " << (int)&c_l_b << endl;
}