class Solution
{
public:
    vector<int> sortArrayByParityII(vector<int> &nums)
    {
        stack<int> even;
        stack<int> odd;

        for (auto it : nums)
        {
            if (it % 2 == 0)
            {
                even.push(it);
            }
            else
            {
                odd.push(it);
            }
        }

        vector<int> ans;

        for (int i = 0; i < nums.size(); i++)
        {
            if (i % 2 == 0)
            {
                ans.push_back(even.top());
                even.pop();
            }
            else
            {
                ans.push_back(odd.top());
                odd.pop();
            }
        }
        
        return ans;
    }
};
