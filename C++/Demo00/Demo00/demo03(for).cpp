#include<iostream>
using namespace std;

int main() {
	system("pause");
	for (int i = 1; i < 100; i++) {
		if ((i / 10 == 7) || (i % 10 == 7) || (i == 7) || (i % 7 == 0)) {
			cout << i << "ÇÃ×À×Ó" << endl;
			
		}
	}
	return  0;
}