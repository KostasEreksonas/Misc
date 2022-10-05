#include <iostream>
#include <bits/stdc++.h>

std::string Palindrome(std::string S) {

	// Store String in variable
	std::string P = S;

	// Reverse string
	reverse(P.begin(), P.end());

	if (S == P) {
		return "Yes\n";
		//std::cout << S << " is not a palindrome.\n";
	}
	else {
		return "No\n";
		//std::cout << S << " is a palindrome.\n";
	}
}

int main() {
	std::string S;
	std::cout << "Enter string: ";
	std::cin >> S;
	std::cout << Palindrome(S);
	return 0;
}
