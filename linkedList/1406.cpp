#include <iostream>

using namespace std;

class Node {
private:
	char ch;
	Node* before;
	Node* next;

public:
	Node(char ch, Node *before, Node *next) {
		this->ch = ch;
		this->before = before;
		this->next = next;
	}

	void setValue(char ch);
	char getValue();
	void setBefore(Node* node);
	Node* getBefore();
	void setNext(Node* node);
	Node* getNext();
};

void Node::setValue(char ch) {
	this->ch = ch;
}

char Node::getValue() {
	return this->ch;
}

void Node::setBefore(Node* node) {
	this->before = node;
}

Node* Node::getBefore() {
	return this->before;
}

void Node::setNext(Node* node) {
	this->next = node;
}

Node* Node::getNext() {
	return this->next;
}

int main() {
	string str; 
	int m;
	cin >> str >> m;

	Node* beforeNode = new Node(NULL, NULL, NULL);
	Node* head = beforeNode;
	Node* currentNode = NULL;

	int i;
	for (i = 0; i < str.length(); i++) {
		currentNode = new Node(str[i], beforeNode, NULL);
		currentNode->getBefore()->setNext(currentNode);
		beforeNode = currentNode;
	}

	while (m--) {
		char cmd;
		cin >> cmd;

		switch (cmd)
		{
		case 'L':
			if (currentNode->getBefore()) {
				currentNode = currentNode->getBefore();
			}
			break;
		case 'D':
			if (currentNode->getNext()) {
				currentNode = currentNode->getNext();
			}
			break;
		case 'B':
			if (currentNode->getValue()) {
				Node* nodeBefore = currentNode->getBefore();
				Node* nodeNext = currentNode->getNext();
				if (nodeNext) {
					nodeBefore->setNext(nodeNext);
					nodeNext->setBefore(nodeBefore);
				}
				else {
					nodeBefore->setNext(NULL);
				}
				currentNode = nodeBefore;
			}
			break;
		case 'P':
			char ch;
			cin >> ch;

			Node* nodeBefore = currentNode->getBefore();
			Node* nodeNext = currentNode->getNext();
			Node* newNode = new Node(ch, currentNode, nodeNext);
			currentNode->setNext(newNode);
			if (nodeNext) {
				nodeNext->setBefore(newNode);
			}
			currentNode = newNode;
			break;
		}
	}

	currentNode = head;
	while (currentNode->getNext()) {
		cout << currentNode->getNext()->getValue();
		currentNode = currentNode->getNext();
	}

	return 0;
}