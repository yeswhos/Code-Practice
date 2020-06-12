#include<iostream>
#include<string>
using namespace std;

struct Student {
	string name;
	int age;
};

struct Teacher {
	string name;
	int age;
	Student stu;
};

int main() {
	Teacher t;
	t.name = "Fanhui";
	t.age = 23;
	t.stu.name = "Lulu";
	t.stu.age = 23;
	Teacher* p = &t;
	cout << "Teacher " << t.name << t.age << "\n" << "Student " << p->stu.name << t.stu.age << endl;
	system("pause");
	return 0;
}