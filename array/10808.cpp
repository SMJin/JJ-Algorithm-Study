#include <iostream>

using namespace std;

int* _10808();

int main() {
	int *result = _10808();

	return 0;
}

int* _10808() {
	const int ALPHABET_SIZE = 26;

	string _input = "";
	cin >> _input;

	int result[ALPHABET_SIZE] = { 0, };

	for (int i = 0; i < _input.size(); i++) {
		result[_input[i] % 'a'] ++;
	}

	for (int i = 0; i < ALPHABET_SIZE; i++) {
		cout << result[i] << " ";
	}

	return result;
}