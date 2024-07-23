class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_set<int> m;

        for (auto it : nums)
        {
            if (m.find(it) != m.end())
            {
                return true;
            }

            m.insert(it);
        }

        return false;
    }
};