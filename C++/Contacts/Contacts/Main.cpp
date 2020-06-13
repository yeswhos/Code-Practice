#include<iostream>
using namespace std;

void showMenu() {
	cout << "**********************************" << endl;
	cout << "Add Contact" << endl;
	cout << "Show Contacts" << endl;
	cout << "Delete Contacts" << endl;
	cout << "Search Contact" << endl;
	cout << "Modify Contact" << endl;
	cout << "Clear All Contact" << endl;
	cout << "Exit" << endl;
	cout << "**********************************" << endl;
}

int main() {
	showMenu();
	system("pause");
	return 0;
}