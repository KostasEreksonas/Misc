#include <iostream>

void bubblesort(int arr[], int size) {

	int temp = 0;
	for (int i = 0; i < size-1; i++) {
		for (int j = 0; j < size-1; j++) {
			if (arr[j] > arr[j+1]) {
				temp = arr[j+1];
				arr[j+1] = arr[j];
				arr[j] = temp;
			}
		}
	}

	for (int r = 0; r < size; r++) {
		std::cout << arr[r] << " ";
	}
	std::cout << "\n";
}

int main() {

	int arr[5] = { 5, 1, 4, 2, 8 };
	int size = sizeof(arr) / sizeof(arr[0]);

	bubblesort(arr, size);

	return 0;

}
