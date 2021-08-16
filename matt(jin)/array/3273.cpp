#include <iostream>

using namespace std;

int main() {
	int n, x;
	cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; i++) cin >> arr[i];
	cin >> x;
	int* arr2 = new int[x + 1]{};
	for (int i = 0; i < n; i++) if (arr[i] <= x) arr2[arr[i]]++;

	int result = 0;
	for (int i = 1; i < (x+1) / 2; i++) if (arr2[i] && arr2[x - i]) result++;

	if (arr2[0] && arr2[x]) result++;
	cout << result;	
	return 0;
}