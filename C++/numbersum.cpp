#include <iostream>

int sum(int &number) {

	int digit;
	int result = 0;

	while ( number != 0) {
		digit = number % 10;
		result += digit;
		number = number / 10;
	}

	return result;

}

int main() {

	int number;
	std::cout << "Enter number: ";
	std::cin >> number;

	std::cout << sum(number) << std::endl;

	return 0;

}
