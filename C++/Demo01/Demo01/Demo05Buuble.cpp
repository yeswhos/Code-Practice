#include<iostream>
using namespace std;

void bubble(int* arr, int len) {
	for (int i = 0; i < len - 1; i++) {
		for (int j = 0; j < len - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

void printArray(int* arr, int len) {
	for (int i = 0; i < len; i++) {
		cout << arr[i] << endl;
	}
}
int main() {
	int arr[5] = { 4, 3, 7, 2, 1 };
	int len = sizeof(arr) / sizeof(arr[0]);
	bubble(arr, len);
	printArray(arr, len);
	system("pause");
	return 0;
}