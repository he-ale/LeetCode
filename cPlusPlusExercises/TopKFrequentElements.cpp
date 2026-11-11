#include <vector>
#include <map>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        map<int, int> frequencies;

        for (int num: nums){
            frequencies[num]++;
        }

        priority_queue <pair<int, int>> pq;

        for(auto& item: frequencies){
            pq.push({item.second, item.first});
        }

        vector<int> result;

        while (k--)
        {
            result.push_back(pq.top().second);
            pq.pop();
        }
        return result;
    }
};