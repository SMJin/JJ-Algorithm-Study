#include <iostream>

using namespace std;

bool isSameLength(string strA, string strB);

int main() {
	int n;
	cin >> n;

	while (n--) {
		string strA, strB;
		cin >> strA >> strB;

		bool isPossible = false;

		if (isSameLength(strA, strB)) {
			int arr[26] = { 0, };
			for (int i = 0; i < strA.size(); i++) {
				arr[(strA[i] % 'a')] ++;
				arr[(strB[i] % 'a')] --;
			}

			isPossible = true;
			for (int a : arr) {
				if (a != 0) {
					isPossible = false;
					break;
				}
			}
		}

		cout << (isPossible ? "Possible" : "Impossible") << endl;
	}

	return 0;
}

bool isSameLength(string strA, string strB) {
	return (strA.length() == strB.length());
}