#include<iostream>
#include<string>
using namespace std;

struct Student {
	string name;
	int age;
};

void printValue(Student s) {
	s.age = 85;
	cout << "printValue" << s.name << s.age << endl;
}

void printAddress(const Student* s) {
	//s->age = 80;
	cout << "printAddress" << s->name << s->age << endl;
}

int main() {
	Student stu = { "Fanhui", 23 };
	cout << "print main before " << stu.name << stu.age << endl;
	printValue(stu);
	Student* p = &stu;
	printAddress(p);
	cout << "print main after" << stu.name << stu.age << endl;
}