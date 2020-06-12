#include<iostream>
#include<string>
using namespace std;

struct Student {
	string name;
	int age;
};

int main() {
	struct Student stuArray[2] = {
		{"Fanhui", 23},
		{"Lulu", 23}
	};
	stuArray[0].name = "Meng";
	for (int i = 0; i < sizeof(stuArray); i++) {
		cout << stuArray[i].name << "\n" << stuArray[i].age << endl;
	}
	system("pause");
	return 0;
}