class Solution
{
public:
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_set<int> n2;
     
        for (auto it : nums2)
        {
            n2.insert(it);
        }

        set<int> s;
     
        for (auto it : nums1)
        {
            if (n2.find(it) != n2.end())
            {
                s.insert(it);
            }
        }

        vector<int> ans;

        for (auto it : s)
        {
            ans.push_back(it);
        }

        return ans;

    }
};