#include <iostream>
#include <vector>

void Longest() {

	// Initialize a vector with weekdays
	std::vector<std::string> days{"Pirmadienis", "Antradienis", "Treciadienis", "Ketvirtadienis", "Penktadienis", "Sestadienis", "Sekmadienis"};

	// Initialize integers to store string lengths
	int max = 0;
	int length = 0;

	// Declare day variable to store longest day
	std::string day;

	for (int i = 0; i < days.size(); i++) {
		length = days[i].length();
		if (length > max) {
			max = length;
			day = days[i];
		}
	}

	std::cout << "Longest day is " << day << " with a length of " << max << ".\n";

}

int main() {

	Longest();

	return 0;

}
