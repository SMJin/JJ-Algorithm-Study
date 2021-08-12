#include <iostream>

using namespace std;

class Code {
private:
	char ch;
	Code* left;
	Code* right;
public:
	Code(char ch, Code* left, Code* right) {
		this->ch = ch;
		this->left = left;
		this->right = right;
	}
	void setValue(char ch);
	void setLeft(Code* left);
	void setRight(Code* right);

	char getValue();
	Code* getLeft();
	Code* getRight();
};

void Code::setValue(char ch) {
	this->ch = ch;
}
void Code::setLeft(Code* left) {
	this->left = left;
}
void Code::setRight(Code* right) {
	this->right = right;
}

char Code::getValue() {
	return this->ch;
}
Code* Code::getLeft() {
	return this->left;
}
Code* Code::getRight() {
	return this->right;
}

int main() {
	int n;
	cin >> n;

	while (n--) {
		string str;
		cin >> str;

		Code* head = new Code( NULL, NULL, NULL );
		Code* cursor = head;
		for (char ch : str) {
			switch (ch)
			{
			case '<':
				if (cursor->getLeft()) {
					cursor = cursor->getLeft();
				}
				break;
			case '>':
				if (cursor->getRight()) {
					cursor = cursor->getRight();
				}
				break;
			case '-':
				if (cursor->getValue()) {
					Code* cursorLeft = cursor->getLeft();
					Code* cursorRight = cursor->getRight();
					cursorLeft->setRight(cursorRight);
					if (cursorRight) {
						cursorRight->setLeft(cursorLeft);
					}
					cursor = cursorLeft;
				}
				break;
			default:
				Code* addCode;
				if (cursor->getRight()) {
					addCode = new Code(ch, cursor, cursor->getRight());
					cursor->getRight()->setLeft(addCode);
				}
				else {
					addCode = new Code(ch, cursor, NULL);
				}
				cursor->setRight(addCode);
				cursor = addCode;
				break;
			}
		}

		while (head->getRight()) {
			cout << head->getRight()->getValue();
			head = head->getRight();
		}
		cout << endl;
	}

	return 0;
}