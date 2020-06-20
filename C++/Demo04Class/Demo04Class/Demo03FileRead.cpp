#include<iostream>
using namespace std;
#include<fstream>
#include<string>

void test() {
	ifstream ifs;
	ifs.open("test.txt", ios::in);
	if (!ifs.is_open()) {
		cout << "Fail" << endl;
		return;
	}
	//1
	char buf[1024] = { 0 };
	while (ifs >> buf) {
		cout << buf << endl;
	}
	//2
	while (ifs.getline(buf, sizeof(buf))) {
		cout << buf << endl;
	}
	//3
	string buff;
	while (getline(ifs, buff)) {
		cout << buff << endl;
	}
	ifs.close();
}

int main() {
	test();
	system("pause");
	return 0;
}
