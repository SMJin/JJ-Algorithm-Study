#include <iostream>

using namespace std;

int main() {
	int n, size;
	cin >> n >> size;
	int arr[2][6] = { 0, };
	int result = 0;

	while (n--) {
		int sex, grade;
		cin >> sex >> grade;

		if (arr[sex][grade - 1] == size) {
			arr[sex][grade - 1] = 0;
			result++;
		}
		else if (!arr[sex][grade - 1]) {
			result++;
		}

		arr[sex][grade - 1] ++;
	}

	cout << result;
	return 0;
}