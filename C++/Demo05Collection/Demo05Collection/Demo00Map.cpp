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
	//copy
	map<int, int>m2(m);

	//copy2
	map<int, int>m3;
	m3 = m;
}

int main() {
	map00();
	system("pause");
	return 0;
}