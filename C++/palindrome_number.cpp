#include <iostream>

void palindrome(int number) {

	// Make copy of a number
	int copy = number;
	// Initialize palindrome variable with a value of 0
	int palindrome = 0;

	// Reverse number and store it in palindrome variable
	while (copy != 0) {
		int digit = copy % 10;
		palindrome = 10 * palindrome + digit;
		copy = copy / 10;
	}

	if (palindrome == number) {
		std::cout << number << " is a palindrome.\n";
	}
	else {
		std::cout << number << " is not a palindrome.\n";
	}
}

int main() {

	// Define variable for number
	int num;
	std::cout << "Enter number: ";
	std::cin >> num;
	palindrome(num);
	return 0;

}
