#include<iostream>
using namespace std;
#define MAX 1000
void showMenu() {
	cout << "**********************************" << endl;
	cout << "1. Add Contact" << endl;
	cout << "2. Show Contacts" << endl;
	cout << "3. Delete Contacts" << endl;
	cout << "4. Search Contact" << endl;
	cout << "5. Modify Contact" << endl;
	cout << "6. Clear All Contact" << endl;
	cout << "0. Exit" << endl;
	cout << "**********************************" << endl;
}

struct Person {
	string Name;
	int Sex;
	int age;
	string phoneNumber;
	string Address;
};

struct AddressBook {
	Person p[MAX];
	int len;
};

void addPerson(AddressBook* abs) {
	if (abs->len == MAX) {
		cout << "Already full, cannot add" << endl;
		return;
	}
	else {
		string name;
		cout << "Please input name" << endl;
		cin >> name;
		abs->p[abs->len].Name = name;

		int sex;
		cout << "Please input sex" << endl;
		cout << "0 is female, 1 is male" << endl;
		cin >> sex;
		while (true)
		{
			if (sex == 1 || sex == 0) {
				abs->p[abs->len].Sex = sex;
				break;
			}
			else {
				cout << "Please re-input sex";
			}
		}

		int age;
		cout << "Please input age" << endl;
		cin >> age;
		abs->p[abs->len].age = age;

		string number;
		cout << "Please input number" << endl;
		cin >> number;
		abs->p[abs->len].phoneNumber = number;

		string address;
		cout << "Please input address" << endl;
		cin >> address;
		abs->p[abs->len].Address = address;
		abs->len++;
		cout << "Ìí¼Ó³É¹¦" << endl;
		system("pause");
		system("cls");
	}
}
int main() {
	int select = 0;
	AddressBook abs;
	abs.len = 0;
	while (true) {
		showMenu();
		cin >> select;
		switch (select) {
			case 1:
				addPerson(&abs);
				break;
			case 2:
				break;
			case 3:
				break;
			case 4:
				break;
			case 5:
				break;
			case 6:
				break;
			case 0:
				cout << "See ya" << endl;
				system("pause");
				return 0;
				break;
			default:
				break;
		}
	}

}