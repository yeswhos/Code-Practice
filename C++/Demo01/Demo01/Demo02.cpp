#include <iostream>
using namespace std;

int main() {
	int a = 10;
	int b = 20;

	const int* p = &a;
	p = &b;

	int * const p2 = &a;
	*p2 = 100;

	const int* const p3 = &a;

	system("pause");
	return 0;
}