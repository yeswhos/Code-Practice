#include<iostream>
#include<string>
#include<random>
#include <time.h>
using namespace std;

struct Student {
	string name;
	int score;
};

struct Teacher {
	string name;
	struct Student arr[5];
};

void inputValue(Teacher t [], int len) {
	string nameSeed = "ABCDE";
	for (int i = 0; i < len; i++) {
		t[i].name = "Teacher ";
		t[i].name += nameSeed[i];
		for (int j = 0; j < 5; j++) {
			t[i].arr[j].name = "Student ";
			t[i].arr[j].name += nameSeed[i];
			int random = rand() % 61 + 41;
			t[i].arr[j].score = random;
		}
	}
}

void printInfo(struct Teacher t[], int len) {
	for (int i = 0; i < len; i++) {
		cout << "Ãû×Ö" << t[i].name << endl;
		for (int j = 0; j < 5; j++) {
			cout << "Ãû×Ö: " << t[i].arr[j].name << t[i].arr[j].score << endl;
		}
	}
}
int main() {
	srand((unsigned int)time(NULL));
	struct Teacher t[3];
	int len = sizeof(t) / sizeof(t[0]);
	inputValue(t, len);
	printInfo(t, len);
	system("pause");
	return 0;
}