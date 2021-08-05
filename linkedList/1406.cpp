#include <iostream>

using namespace std;

int main() {
	string str; 
	int m;
	cin >> str >> m;
	//cout << "str : " << str << endl;

	char *arr = new char[100000];
	int str_length = str.length();
	int size = str.length();
	for (int i = 0; i < str.length(); i++) {
		*arr = str[i];
		arr++;
	}
	arr--;

	while (m--) {
		char ch;
		cin >> ch;

		switch (ch)
		{
		case 'L':
			if (size > 0) {
				arr--;
				size--;
			}
			//cout << "*arr : " << *arr << endl;
			//cout << "size : " << size << endl;
			//cout << "str_length : " << str_length << endl;
			break;	
		case 'D':
			if (size < str_length) {
				arr++;
				size++;
			}
			//cout << "*arr : " << *arr << endl;
			//cout << "size : " << size << endl;
			//cout << "str_length : " << str_length << endl;
			break;
		case 'B':
			if (size) {
				if (str_length == size) {
					arr--;
					size--;
				}
				else {
					char next_char;
					int current_cursor = size;
					for (int i = current_cursor; i < str_length; i++) {
						arr++;
						next_char = *arr;
						arr--;

						*arr = next_char;
						size++;
						arr++;
					}
					for (int i = current_cursor; i <= str_length; i++) {
						arr--;
						size--;
					}
				}
				str_length--;
			}
			
			//cout << "*arr : " << *arr << endl;
			//cout << "size : " << size << endl;
			//cout << "str_length : " << str_length << endl;
			break;
		case 'P':
			char add_char, cur_char;
			cin >> add_char;

			arr++;
			size++;
			int current_cursor = size;
			for (int i = current_cursor; i <= str_length; i++) {
				cur_char = *arr;
				*arr = add_char;
				add_char = cur_char;
				arr++;
				size++;
			}
			*arr = add_char;

			for (int i = current_cursor; i <= str_length; i++) {
				arr--;
				size--;
			}
			str_length++;

			//cout << "*arr : " << *arr << endl;
			//cout << "size : " << size << endl;
			//cout << "str_length : " << str_length << endl;
			break;
		}
	}

	while (size) {
		size--;
		arr--;
	}
	size++;
	arr++;

	for (int i = 0; i < str_length; i++) {
		cout << *arr;
		arr++;
		size++;
	}

	return 0;
}