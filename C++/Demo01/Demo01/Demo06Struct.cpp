#include<iostream>
using namespace std;

struct student
{
	string name;
	int age;
}s3;

int main() {
	struct student s1;
	s1.name = "Fanhui";
	s1.age = 23;
	cout << "student 1" << s1.name << s1.age << endl;

	struct student s2 = { "Lulu", 23 };
	cout << "student 2" << s2.name << s2.age << endl;

	s3.name = "Fanhui";
	s3.age = 24;
	cout << "student 3" << s3.name << s3.age << endl;

	system("pause");
	return 0;
}