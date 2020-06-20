#include<fstream>
#include<iostream>
using namespace std;

int main() {
	ofstream ofs;
	ofs.open("test.txt", ios::out);
	ofs << "aaa" << endl;
	ofs.close();
	system("pause");
	return 0;
}