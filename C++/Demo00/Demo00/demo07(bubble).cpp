#include<iostream>
using namespace std;

int main() {
	int arr[] = { 4, 2, 8, 0, 5, 7, 1, 3, 9 };
	int tmp = 0;
	for (int j = 0; j < 8; j++) {
		for (int i = 0; i < 8; i++) {
			if (arr[i] > arr[i + 1]) {
				tmp = arr[i];
				arr[i] = arr[i + 1];
				arr[i + 1] = tmp;
			}
		}
	}
	for (int i = 0; i < 9; i++) {
		cout << arr[i] << " ";
	}
	system("pause");
	return 0;
}