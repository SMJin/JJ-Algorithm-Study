#include <iostream>

using namespace std;

int main() {
	int n, x;
	cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; i++) cin >> arr[i];
	cin >> x;

	int result = 0;
	for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) if (arr[i] + arr[j] == x) result++;

	cout << result;
	delete[] arr;
	
	return 0;
}