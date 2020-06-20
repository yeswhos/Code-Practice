#include<iostream>
using namespace std;

class Student {
public:
	string m_name;
	int m_id;
	void setNmae(string name) {
		m_name = name;
	}
	void setId(int id) {
		m_id = id;
	}
	void showStudent() {
		cout << m_name << "\t" << m_id << endl;
	}
};

int main() {
	Student s1;
	s1.m_id = 1;
	s1.m_name = "Fanhui";
	s1.showStudent();

	Student s2;
	s2.setId(2);
	s2.setNmae("Lulu");
	s2.showStudent();

	system("pause");
	return 0;
}