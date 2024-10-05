class Solution
{
public:
    vector<int> relativeSortArray(vector<int> &arr1, vector<int> &arr2)
    {
        unordered_map<int, int> m;
        
        for (auto it : arr1)
        {
            m[it]++;
        }

        vector<int> ans;

        for (auto it : arr2)
        {
            for (int i = 0; i < m[it]; i++)
            {
                ans.push_back(it);
            }
            m[it] *= -1;
        }

        vector<int> temp;
        for (auto it : m)
        {
            if (it.second > 0)
            {
                temp.push_back(it.first);
            }
        }

        sort(temp.begin(), temp.end());

        for (auto it : temp)
        {
            for (int i = 0; i < m[it]; i++)
            {
                ans.push_back(it);
            }
        }

        return ans;

    }
};