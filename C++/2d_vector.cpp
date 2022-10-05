// C++ code to demonstrate 2D vector 
#include <iostream> 
#include <vector> // for 2D vector 
using namespace std; 
  
int main() 
{ 
    int a = 0;
    int b = 0;
    // Initializing 2D vector "vect" with 
    // values 
    vector<vector<int> > vect{ { 1, 2, 3 }, 
                               { 4, 5, 6 }, 
                               { 7, 8, 9 } }; 
  
    // Displaying the 2D vector 
    for (int i = 0; i < vect.size(); i++) { 
        a = 0;
	for (int j = 0; j < vect[i].size(); j++) {
		a += vect[i][j];
		cout << a << endl;
	}
    }
    return 0; 
}
