#include <iostream>
#include <string>
#include <vector>

int main() {
	std::vector<std::vector<char>> board  = {{'s', 'o', 's', 'o'},
											 {'s', 'o', 'o', 's'},
											 {'s', 's', 's', 's'}};
	std::vector<char> word;
	for (int i = 0; i < board.size(); i++) {
		for (int j = 0; j < board[i].size(); j++) {
			word = board[i][j] + board [i][j];
			std::cout << word;
		}
	}
	return 0;
}
