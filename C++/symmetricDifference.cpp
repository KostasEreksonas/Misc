#include <iostream>
#include <vector>

void symmetric(std::vector<int> &vect1, std::vector<int> &vect2, int &size1, int &size2) {

	// Declare vector to store symmetric difference between given arrays
	std::vector<int> symdiff;
	int i = 0, j = 0;

	while (i < size1 && j < size2) {
		if (vect1[i] < vect2[j]) {
			symdiff.push_back(vect1[i]);
			i++;
		}
		else if (vect2[j] < vect1[i]) {
			symdiff.push_back(vect2[j]);
			j++;
		}
		else {
			i++;
			j++;
		}
	}

	if (vect1[size1-1] > vect2[size2-1]) {
		symdiff.push_back(vect1[size1-1]);
	}
	else if (vect1[size1-1] < vect2[size2-1]) {
		symdiff.push_back(vect2[size1-1]);
	}

	std::cout << "Symmetric difference of given vectors is: ";
	for (int r = 0; r < symdiff.size(); r++) {
		std::cout << symdiff[r] << " ";
	}
	std::cout << "\n";
}

int main() {

	std::vector<int> vect1{1,2,4,5};
	std::vector<int> vect2{1,2,3,6};
	int size1 = vect1.size();
	int size2 = vect2.size();

	symmetric(vect1,vect2,size1,size2);

	return 0;

}
