#include<iostream>
using namespace std;
#include<fstream>

void test() {
	ifstream ifs;
	ifs.open("test.txt", ios::in);
	if (!ifs.is_open()) {
		cout << "Fail" << endl;
		return;
	}
	char buf[1024] = { 0 };
	while (ifs >> buf) {
		cout << buf << endl;
	}

	ifs.close();
}

int main() {
	test();
	system("pause");
	return 0;
}
