#include <iostream>

using namespace std;

class Deque {
private:
	int head;
	int tail;
	int* arr;
public:
	Deque(int n) {
		this->head = n/2;
		this->tail = n/2;
		this->arr = new int[n*2];
	}

	void push_front(int x);
	void push_back(int x);
	int pop_front();
	int pop_back();
	int size();
	int empty();
	int front();
	int back();

};

void Deque::push_front(int x) {
	arr[--head] = x;
}

void Deque::push_back(int x) {
	arr[tail++] = x;
}

int Deque::pop_front() {
	if (this->empty()) return -1;
	return arr[head++];
}

int Deque::pop_back() {
	if (this->empty()) return -1;
	return arr[--tail];
}

int Deque::size() {
	return tail - head;
}

int Deque::empty() {
	return !this->size();
}

int Deque::front() {
	return arr[head];
}

int Deque::back() {
	return arr[tail-1];
}

int main() {
	int n;
	cin >> n;

	Deque* dq = new Deque(n);

	while (n--) {
		char ch;
		cin >> ch;

		switch (ch)
		{
		case 'p':
			char ch2, ch3;
			cin >> ch2;
			cin.ignore(LLONG_MAX, '_');
			cin >> ch3;
			switch (ch2)
			{
			case 'u':
				cin.ignore(LLONG_MAX, ' ');
				int i;
				cin >> i;
				if (ch3 == 'f') {
					dq->push_front(i);
					break;
				}
				else {
					dq->push_back(i);
					break;
				}
			case 'o':
				cin.ignore(LLONG_MAX, '\n');
				if (ch3 == 'f') {
					std::cout << dq->pop_front() << endl;
					break;
				}
				else {
					std::cout << dq->pop_back() << endl;
					break;
				}
			default:
				std::cout << "Unvalid command !! in pu/o" << endl;
				break;
			}
			break;
		case 's':
			std::cout << dq->size() << endl;
			cin.ignore(LLONG_MAX, '\n');
			break;
		case 'e':
			std::cout << dq->empty() << endl;
			cin.ignore(LLONG_MAX, '\n');
			break;
		case 'f':
			std::cout << dq->front() << endl;
			cin.ignore(LLONG_MAX, '\n');
			break;
		case 'b':
			std::cout << dq->back() << endl;
			cin.ignore(LLONG_MAX, '\n');
			break;
		default:
			break;
		}
	}

	return 0;
}