#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <regex>

using namespace std; // Para simplificar la lectura en el ejemplo

class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        // 1. Convertir a minúsculas con C++20 Ranges (¡Perfecto!)
        ranges::transform(paragraph, paragraph.begin(), [](unsigned char c) {
            return tolower(c);
        });

        unordered_set<string> ban(banned.begin(), banned.end());
        
        regex expresion("[a-z]+");
        unordered_map<string, int> words;
        
        int max = 0;
        string result = "";

        for (sregex_iterator it(paragraph.begin(), paragraph.end(), expresion), fin; it != fin; ++it) {
            const string e = it->str();
            
            if (!ban.contains(e)) {
                words[e]++; 
                
                if (words[e] > max) {
                    max = words[e];
                    result = e;
                }
            }
        }

        return result;
    }
};
