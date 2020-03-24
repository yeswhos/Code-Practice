#include<iostream>
#include<math.h>
using namespace std;
int main() {
	system("pause");
	int num = 100;
	do {
		int a = num / 100;
		int b = (num / 10) % 10;
		int c = (num % 100) % 10;
		a = pow(a, 3);
		b = pow(b, 3);
		c = pow(c, 3);

		//cout << b << endl;
		//cout << (b ^ 3) << endl;
		//cout << (c ^ 3) << endl;
		int num_fake = a + b + c;
		//cout << a  << "\n" << b << "\n" << c << "\n" << num_fake << "\n" << num << endl;
		if (num_fake == num) {
			cout << "this is flower number: " << num << endl;
			num++;
		}
		else {
			num++;
		}
	} while (num < 1000);
	return 0;
}