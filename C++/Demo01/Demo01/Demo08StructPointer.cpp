#include<iostream>
#include<string>
using namespace std;

struct Student {
	string name;
	int age;
};

int main() {
	struct Student stu = { "Fanhui", 23 };
	Student * p = &stu;
	cout << p->name << p->age << endl;
	system("pause");
	return 0;
}