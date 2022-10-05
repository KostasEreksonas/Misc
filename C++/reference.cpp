#include <iostream>

void square(int &i) {
	i = i * i;
}

int main() {

	int num = 5;

	square(num);

	std::cout << num << "\n";

}
