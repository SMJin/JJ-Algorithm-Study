#include <iostream>

using namespace std;

class Que {
private:
	int head;
	int tail;
	int* arr;
public:
	Que(int n) {
		this->head = 0;
		this->tail = 0;
		this->arr = new int[n];
	}

	void push(int x);
	int pop();
	int size();
	bool empty();
	int front();
	int back();
};

void Que::push(int x) {
	this->arr[tail++] = x;
}

int Que::pop() {
	if (this->empty()) {
		return -1;
	}
	return this->arr[head++];
}

int Que::size() {
	return this->tail - this->head;
}

bool Que::empty() {
	return !this->size();
}

int Que::front() {
	if (this->empty()) {
		return -1;
	}
	return this->head;
}

int Que::back() {
	if (this->empty()) {
		return -1;
	}
	return this->tail;
}

int main() {
	int n;
	cin >> n;

	Que* q = new Que(n*2);

	int i;
	for (i = 1; i <= n; i++) {
		q->push(i);
	}

	for (i = 1; i < n; i++) {
		q->pop();
		q->push(q->pop());
	}

	cout << q->pop();

	return 0;
}