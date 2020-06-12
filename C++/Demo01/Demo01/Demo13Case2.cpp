#include<iostream>
#include<string>
using namespace std;
struct Hero {
	string name;
	int age;
	string sex;
};

struct Hero hArray[5] = {
	{"����", 23, "��"},
	{"����", 22, "��"},
	{"�ŷ�", 20, "��"},
	{"����", 21, "��"},
	{"����", 19, "Ů"}
};

void printArray(struct Hero hArray[], int len) {
	for (int i = 0; i < len; i++) {
		cout << "���֣�" << hArray[i].name << hArray[i].age << hArray[i].sex << endl;
	}
}

void bubble(Hero hArray[], int len) {
	for (int i = 0; i < len - 1; i++) {
		for (int j = 0; j < len - i - 1; j++) {
			
			if (hArray[j].age > hArray[j + 1].age) {
				//int temp = hArray[i].age;
				//hArray[j].age = hArray[j + 1].age;
				//hArray[j + 1].age = temp;
				struct Hero temp = hArray[j];
				hArray[j] = hArray[j + 1];
				hArray[j + 1] = temp;
			}
		}
	}
}

int main() {
	int len = sizeof(hArray) / sizeof(hArray[0]);
	printArray(hArray, len);
	bubble(hArray, len);
	printArray(hArray, len);
	system("pause");
	return 0;
}
