#include<iostream>
#include<map>
using namespace std;

void printMap(map<int, int>& m) {
	for (map <int, int>::iterator it = m.begin(); it != m.end(); it++) {
		cout << it->first << '\t' << it->second << endl;
	}
	cout << endl;
}

void test01() {
	map<int, int>m;
	m.insert(pair<int, int>(1, 10));
	m.insert(make_pair(2, 20));
	m.insert(map<int, int>::value_type(3, 30));
	m[4] = 40;
	printMap(m);

	m.erase(m.begin());
	printMap(m);

	m.erase(3);
	printMap(m);

	m.erase(m.begin(), m.end());
	printMap(m);
}

int main() {
	test01();
	system("pause");
	return 0;
}