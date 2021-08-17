#include <iostream>
#include <stack>

using namespace std;
	
int main() {
	int k;
	cin >> k;

	stack<int> stack;
	string result = "";
	int* input_numbers = new int[k];
	bool isNo = false;
	int current = 1;

	for (int i = 0; i < k; i++) {
		int n;
		cin >> n;
		input_numbers[i] = n;
	}

	for (int i = 0; i < k; i++) {

		while (current <= input_numbers[i]) {
			stack.push(current);
			result += "+\n";
			current++;
		}

		if (stack.top() == input_numbers[i]) {
			stack.pop();
			result += "-\n";
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
		cout << result;
	}

	return 0;
}