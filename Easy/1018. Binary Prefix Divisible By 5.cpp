class Solution
{
public:
    vector<bool> prefixesDivBy5(vector<int> &nums)
    {
        vector<bool> ans;

        int temp = 0;

        for (auto it : nums)
        {
            temp = (temp * 2 + it) % 5;
            if (temp == 0)
            {
                ans.push_back(true);
            }
            else
            {
                ans.push_back(false);
            }

        }

        return ans;
    }
};
