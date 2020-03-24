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
                cout << "对了" << endl;
                break;
            }
            else if (val < num) {
                cout << "小了" << endl;
            }
            else if (val > num) {
                cout << "大了" << endl;
         }
        }
    return 0;
}