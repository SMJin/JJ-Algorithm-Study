#include <iostream>
#include <stack>

using namespace std;

int main() {
	int n;
	cin >> n;

	stack<int> tower;
	stack<int> tmp;
	stack<int> result;
	for (int i = 0; i < n; i++) {
		int t;
		cin >> t;
		tower.push(t);
	}
	
	for (int i = n; i > 0; i--) {
		int current = tower.top();
		tower.pop();
		int compare = 0;
		if (!tower.empty()) {
			compare = tower.top();
		}

		int howMany = 1;
		while (compare && current > compare) {
			tmp.push(compare);
			tower.pop();
			if (!tower.empty()) {
				compare = tower.top();
				howMany++;
			}
			else {
				compare = NULL;
				howMany = 0;
			}
		}

		if (compare) {
			result.push(i - howMany);
		}
		else {
			result.push(0);
		}

		while (!tmp.empty()) {
			tower.push(tmp.top());
			tmp.pop();
		}

	}

	while (!result.empty()) {
		cout << result.top() << " ";
		result.pop();
	}

	return 0;
}