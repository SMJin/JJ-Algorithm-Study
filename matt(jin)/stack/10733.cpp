#include <iostream>
#include <stack>

using namespace std;

int main() {
	int k;
	cin >> k;

	stack<int> stack;
	string result = "";
	bool isNo = false;
	int current = 1;

	while(k--) {
		int n;
		cin >> n;

		while (current <= n) {
			stack.push(current);
			result += "+";
			current++;
		}

		if (stack.top() == n) {
			stack.pop();
			result += "-";
		}
		else {
			isNo = true;
			break;
		}

	}

	if (isNo) {
		cout << "NO";
	}
	else {
		for (char ch : result) {
			cout << ch << endl;
		}
	}

	return 0;
}