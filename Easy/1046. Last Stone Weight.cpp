class Solution
{
public:
    int lastStoneWeight(vector<int> &stones)
    {
        while (stones.size() > 1)
        {
            sort(stones.begin(), stones.end(), greater<int>());
            
            // for (auto it : stones) cout << it << " ";
            // cout << endl;

            int add = stones[0] - stones[1];
            
            stones.erase(stones.begin());
            stones.erase(stones.begin());
            
            stones.push_back(add);
        }

        return stones[0];
    }
};
