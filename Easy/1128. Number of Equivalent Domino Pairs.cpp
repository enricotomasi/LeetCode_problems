class Solution
{
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes)
    {
        unordered_map<int, int> m;
        
        int ans = 0;
        
        for (auto it : dominoes)
        {
            ans += m[min(it[0], it[1]) * 10 + max(it[0], it[1])]++;
        }
        
        return ans;
    }
};