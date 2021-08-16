#include <iostream>

using namespace std;

struct Node {
	int num;
	struct Node* next;
};

int main() {
	int n, k;
	cin >> n >> k;
	if (n == 1) {
		cout << "<1>";
	}
	else {
		struct Node head = { 1, NULL };
		struct Node* beforeNode = &head;
		for (int i = 2; i <= n; i++) {
			Node* currentNode = new Node;
			currentNode->num = i;
			beforeNode->next = currentNode;
			beforeNode = currentNode;
		}
		beforeNode->next = &head;

		struct Node* cursor = &head;
		cout << '<';

		if (k == 1) {
			for (int i = 1; i < n; i++) {
				cout << cursor->num << ", ";
				cursor = cursor->next;
			}
			cout << cursor->num << '>';
		}
		else {
			while (n--) {
				if (cursor->next) {
					for (int i = 1; i < k - 1; i++) {
						cursor = cursor->next;
					}
					cout << cursor->next->num << ", ";
					if (cursor == cursor->next->next) {
						cursor->next = NULL;
					}
					else {
						cursor->next = cursor->next->next;
						cursor = cursor->next;
					}
				}
				else {
					cout << cursor->num << '>';
				}
			}
		}
	}
}