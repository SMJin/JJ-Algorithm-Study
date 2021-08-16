#include <iostream>

using namespace std;

class Stack {
private:
	int size;
	int arr[10001];
public:
	Stack() {
		this->size = 0;
		this->arr[10001] = { -1, };
	}

	void push(int num);
	int pop();
	int getSize();
	bool isEmpty();
	int peak();
};

int main() {
	int n;
	cin >> n;

	Stack* stack = new Stack();

	while (n--) {
		string command;
		cin >> command;
		if (command == "push") {
			int i;
			cin >> i;
			stack->push(i);
		}
		else if (command == "pop") {
			cout << stack->pop() << endl;
		}
		else if (command == "size") {
			cout << stack->getSize() << endl;
		}
		else if (command == "empty") {
			cout << (int)(stack->isEmpty()) << endl;
		}
		else {
			cout << stack->peak() << endl;
		}
	}

	return 0;
}

void Stack::push(int num) {
	arr[size++] = num;
}

int Stack::pop() {
	if (!this->isEmpty()) {
		return arr[--size];
	}
	return -1;
}

int Stack::getSize() {
	return this->size;
}

bool Stack::isEmpty() {
	return this->getSize() ? false : true;
}

int Stack::peak() {
	if (this->isEmpty()) {
		return -1;
	}
	return arr[size-1];
}