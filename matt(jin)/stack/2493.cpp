#include <iostream>
#include <stack>

using namespace std;

int main() {
	int n;
	cin >> n;

	int* tower = new int[n];
	stack<int> result;
	for (int i = 0; i < n; i++) {
		int t;
		cin >> t;
		tower[i] = t;
	}

	int i;
	for (i = n-1; i > 0; i--) {
		int current = tower[i];
		int compare = 0;

		bool hit = false;

		int j;
		for (j = i - 1; j >= 0; j--) {
			compare = tower[j];
			if (compare >= current) {
				result.push(j + 1);
				hit = true;
				break;
			}
		}

		if (!hit) {
			result.push(0);
		}

	}

	cout << "0";
	while (!result.empty()) {
		cout << " " << result.top();
		result.pop();
	}


	return 0;
}