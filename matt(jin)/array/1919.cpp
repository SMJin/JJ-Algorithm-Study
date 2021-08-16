#include <iostream>

using namespace std;

int main() {
	string strA, strB;
	cin >> strA >> strB;
	int arr[26] = { 0, };
	
	for (char a : strA) arr[a % 'a'] ++;
	for (char b : strB) arr[b % 'a'] --;

	int result = 0;
	for (int i : arr) {
		if (i < 0) i = -i;
		result += i;
	}
	cout << result;

	return 0;
}