#include <iostream>
#include<vector>

using namespace std;

int main() {
	//vector <int> a {-4, -5, 0, -6, -5, -4, -7, 9};
	vector <int> a {6, -5, -5, 5, 10, 5, 1, 8, 6, -2};
	vector <int> b {};
	std::cout << a.size() << std::endl;
	for(int i = 0; i < a.size(); i++) {
		int c = a.operator[](i-1) + a.operator[](i) + a.operator[](i+1);
		b.push_back(c);
		cout << a.operator[](i+1) << " " << b.operator[](i) << endl;
	}
	cout << endl;
	cout << a.operator[](11) << endl;
}
