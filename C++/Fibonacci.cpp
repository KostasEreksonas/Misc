#include<iostream>
#include<bits/stdc++.h>

int fib(int n) {
	if (n <= 1)
		return n;
	return fib(n-1) + fib(n-2);
}

int main () {
	int n;
	std::cout << "Enter Fibonacci number you want to find: ";
	std::cin >> n;
	std::cout << fib(n) << "\n";
	//getchar();
	return 0;
}
