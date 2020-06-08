#include <iostream>;
using namespace std;
int main() {
	int a = 10;
	int * p;
	p = &a;
	cout << "int" << sizeof(int*) << endl;
	cout << "float" << sizeof(float*) << endl;
	cout << "double" << sizeof(double*) << endl;
	cout << "char" << sizeof(char*) << endl;
	system("pause");
	return 0;
}