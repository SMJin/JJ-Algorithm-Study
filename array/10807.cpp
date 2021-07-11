#include <iostream>

using namespace std;

int _10807();

int main() {
	cout << _10807();
	return 0;
}

int _10807() {
	const int N = 100;
	int result = 0;

	int size = 0;
	cin >> size;

	int arr[N] = { 0, };

	for (int i = 0;i < size; i++) {
		cin >> arr[i];
	}

	int v = 0;
	cin >> v;
	
	for (int i=0; i<size; i++) {
		if (arr[i] == v) {
			result++;
		}
	}

	return result;
}