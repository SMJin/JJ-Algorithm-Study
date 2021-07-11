#include <iostream>

using namespace std;

int main(void) {
	const int N = 100;
	int size, n, v;
	cin >> size;

	int arr[N] = { 0, };

	while (size--) {
		cin >> n;
		arr[n] ++;
	}

	cin >> v;
	cout << arr[v];

	return 0;
}