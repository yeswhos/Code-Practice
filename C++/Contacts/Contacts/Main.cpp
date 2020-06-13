#include<iostream>
using namespace std;

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

int main() {
	int select = 0;
	while (true) {
		showMenu();
		cin >> select;
		switch (select) {
			case 1:
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