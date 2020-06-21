#include<map>
#include<iostream>
using namespace std;

void printMap(map<int, int>& m) {
	for (map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
		cout << it->first << '\t' << it->second << endl;
	}
	cout << endl;
}

void map00() {
	map<int, int> m;
	m.insert(pair<int, int>(1, 10));
	m.insert(pair<int, int>(2, 20));
	m.insert(pair<int, int>(3, 30));
	printMap(m);
	
	map<int, int>::iterator pos = m.find(3);
	if (pos != m.end()) {
		cout << "´þµ½" << (*pos).first << "value = " << pos->second << endl;
	}
	else {
		cout << "Î´ÕÒµ½" << endl;
	}

	int num = m.count(3);
	cout << "num = " << num << endl;
}

int main() {
	map00();
	system("pause");
	return 0;
}