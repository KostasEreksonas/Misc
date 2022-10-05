#include <iostream>

int sum(int &num1, int &num2) {

	int result = num1 + num2;

	return result;

}

int main() {

	int num1, num2;

	std::cout << "Enter first number: ";
	std::cin >> num1;

	std::cout << "Enter second number: ";
	std::cin >> num2;

	std::cout << "Sum of " << num1 << " and " << num2 << " is: " << sum(num1, num2) << std::endl;

	return 0;

}
