// C++ program to find the symmetric difference
// of two sorted array.
#include <iostream>
using namespace std;
void symmDiff(int arr1[], int arr2[], int n, int m)
{
	// Traverse both arrays simultaneously.
	int i = 0, j = 0;
	while (i < n && j < m) {
	
		// Print smaller element and move
		// ahead in array with smaller element
		if (arr1[i] < arr2[j]) {
			cout << arr1[i] << " ";
			i++;
		}
		else if (arr2[j] < arr1[i]) {
			cout << arr2[j] << " ";
			j++;
		}

		// If both elements same, move ahead
		// in both arrays.
		else {
			i++;
			j++;
		}
	}
	while (i < n) {
		cout << arr1[i] << " ";
		i++;
	}
	while (j < m) {
		cout << arr2[j] << " ";
		j++;
	}
}

// Driver code
int main()
{
	int arr1[] = { 2, 4, 5, 7, 8, 10, 12, 15 };
	int arr2[] = { 5, 8, 11, 12, 14, 15 };
	int n = sizeof(arr1) / sizeof(arr1[0]);
	int m = sizeof(arr2) / sizeof(arr2[0]);
	symmDiff(arr1, arr2, n, m);
	std::cout << "\n" << n << "\n";
	std::cout << m << "\n";
	std::cout << sizeof(arr1) << " " << sizeof(arr1[0]) << " " << n << "\n";
	std::cout << sizeof(arr2) << " " << sizeof(arr2[0]) << " " << m << "\n";
	return 0;
}
