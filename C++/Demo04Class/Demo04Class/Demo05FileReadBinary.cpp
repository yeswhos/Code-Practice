#include<fstream>
#include<string>
#include<iostream>
using namespace std;

class Person {
public:
	char m_Name[64];
	int m_Age;
};

void test() {
	ifstream ifs;
	ifs.open("person.txt", ios::in | ios::binary);
	if (!ifs.is_open()) {
		return;
	}
	Person p;
	ifs.read((char*)&p, sizeof(Person));
	cout << p.m_Age << "\t" << p.m_Name << endl;
	ifs.close();
}

int main() {
	test();
	system("pause");
	return 0;
}