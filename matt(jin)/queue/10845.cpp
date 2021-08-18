#include <iostream>

using namespace std;

class Queue {
private:
	int f;
	int b;
	int* arr;
public:
	Queue(int n) {
		this->f = 0;
		this->b = 0;
		this->arr = new int[n];
	}

	void push(int x);
	int pop();
	int size();
	bool empty();
	int front();
	int back();
};

void Queue::push(int x) {
	this->arr[this->b++] = x;
}

int Queue::pop() {
	if (f == b) return -1;
	else return this->arr[this->f++];
}

int Queue::size() {
	return this->b - this->f;
}

bool Queue::empty() {
	return !this->size();
}

int Queue::front() {
	if (f == b) return -1;
	else return this->arr[f];
}

int Queue::back() {
	if (f == b) return -1;
	else return this->arr[b - 1];
}

int main() {
	int n;
	cin >> n;

	Queue* q = new Queue(n);

	while (n--) {
		string command;
		cin >> command;
		if (command == "push") {
			int i;
			cin >> i;
			q->push(i);
		}
		else if (command == "pop") {
			cout << q->pop() << endl;
		}
		else if (command == "size") {
			cout << q->size() << endl;
		}
		else if (command == "empty") {
			cout << (int)(q->empty()) << endl;
		}
		else if (command == "front") {
			cout << q->front() << endl;
		}
		else {
			cout << q->back() << endl;
		}
	}

	return 0;
}