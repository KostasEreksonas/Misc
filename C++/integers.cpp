#include <iostream>

int main() {
	int x = 5;
	int y = 4;
	int sum = x + y;
	std::cout << "The sum of " << x << " and " << y << " is " << sum << std::endl;
	int arr[10] = {};
	int a[2][10] = {0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9};
	for (int i=0; i<2; i++) {
		for (int j=0; j<10; j++) {
			std::cout << "Element at array[" << i << "][" << j << "] is: " << a[i][j] << std::endl;
			sum = a[0][j] + a[1][j];
			std::cout << "Sum is: " << sum << std::endl;
		}
	}
	return 0;
}
