//
// Created by ALE on 8/28/2026.
//
#include <vector>
using namespace std;

class SelfDividingNumbers {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> result;
        while (left<=right) {
            if (left % 10 != 0) {
                if (isDividedByItself (left)) {
                    result.push_back(left);
                }
            }
            left++;
        }
        return result;
    }

private:
    bool isDividedByItself (const int num) {
        int index= num;
        while (index > 0) {
            const int aux= index % 10;
            if (aux == 0 || num % aux != 0) {
                return false;
            }
            index = index / 10;
        }
        return true;
    }
};