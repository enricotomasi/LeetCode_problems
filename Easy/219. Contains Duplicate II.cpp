class Solution
{
public:
    bool containsNearbyDuplicate(vector<int> &nums, int k)
    {
        int n = nums.size();
        unordered_map<int, vector<int>> m;

        for (int i  = 0; i < n; i++)
        {
            m[nums[i]].push_back(i);
        }

        for (auto it : m)
        {
            // cout << it.first << "  ### ";
            // for (auto it2: it.second) cout << it2 << " ";
            // cout << endl;

            if (it.second.size() > 1)
            {
                for (int i = 0; i < it.second.size();  i++)
                {
                    for (int j = i + 1; j < it.second.size(); j++)
                    {                       
                        if (abs(it.second[i] - it.second[j]) <= k)
                        {
                            return true;
                        }
                    }
                }
            }

        }

        return false;
    }
};