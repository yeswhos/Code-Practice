#include<iostream>

using namespace std;

int main() {
    system("pause");
    int num = rand() % 10 + 1;
    int val = 0;
        while (1)
        {
            cin >> val;
            if (val == num) {
                cout << "����" << endl;
                break;
            }
            else if (val < num) {
                cout << "С��" << endl;
            }
            else if (val > num) {
                cout << "����" << endl;
         }
        }
    return 0;
}