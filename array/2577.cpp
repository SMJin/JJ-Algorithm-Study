#include <iostream>

using namespace std;

int main() {
	int n = 3;
	int arr[10] = { 0, };
	int result = 1;

	while (n--) {
		int temp = 0;
		cin >> temp;
		result *= temp;
	}

	int max = 100000000;
	bool start = false;
	for (int i = 0; i < 9; i++) {
		if (!start && result / max != 0) {
			start = true;
		}
		if (start) {
			arr[result / max]++;
		}
		result %= max;
		max /= 10;
	}

	for (int i : arr) {
		cout << i << endl;
	}

	return 0;
}