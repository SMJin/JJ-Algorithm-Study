#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	int arr[9] = { 0, };

	if (!n) {
		arr[n] ++;
	}

	while (n) {
		int cur = n % 10;
		if (cur == 9) {
			cur = 6;
		}
		arr[cur] ++;
		n /= 10;
	}

	if (arr[6] % 2 != 0) arr[6]++;
	arr[6] /= 2;

	int result = 0;
	for (int a : arr) {
		if (result < a) {
			result = a;
		}
	}

	cout << result;

	return 0;
}