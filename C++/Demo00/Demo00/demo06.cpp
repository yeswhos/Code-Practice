#include<iostream>
using namespace std;

int main() {
	int arr[] = {1, 2, 3, 4, 5};
	int tmp = 0;
	int start = 0;
	int end = 4;
	for (int i = 0; i < 3; i++) {
		tmp = arr[i];
		arr[i] = arr[end];
		arr[end] = tmp;
		end--;
	}
	for (int i = 0; i < 5; i++) {
		cout << arr[i] << endl;
	}
	
	system("pause");
	return 0;
}