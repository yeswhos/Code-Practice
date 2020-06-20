#include<iostream>
#include<fstream>
using namespace std;

class Person {
public:
	char m_Nmae[64];
	int m_Age;
};

void test01() {
	ofstream ofs;
	ofs.open("person.txt", ios::out | ios::binary);
	Person p = { "Fanhui", 23 };
	ofs.write((const char*)&p, sizeof(Person));
	ofs.close();
}

int main() {
	test01();
	system("pause");
	return 0;
}