class Solution
{
public:
    vector<string> summaryRanges(vector<int> &nums)
    {
        int n = nums.size();

        if (n == 0)
        {
            return { };
        }

        if (n == 1)
        {
            return { to_string(nums[0]) };
        }
        
        vector<string> ans;

        if (n == 2)
        {
            if (nums[1] - nums[0] == 1)
            {
                return { to_string(nums[0]) + "->" + to_string(nums[1]) };
            }
            else
            {
                ans.push_back(to_string(nums[0]));
                ans.push_back(to_string(nums[1]));

                return ans;
            }
        }
        
        int start = 0;

        for (int i = 1; i < n; i++)
        {
            long long int diff = (long long int)nums[i] - (long long int)nums[i - 1];
            if (diff != 1)
            {
                if (start == i - 1)
                {
                    ans.push_back(to_string(nums[start]));
                }
                else
                {
                    ans.push_back(to_string(nums[start]) + "->" + to_string(nums[i - 1]));
                }

                start = i;
            }
        }

        if (start == n - 1)
        {
            ans.push_back(to_string(nums[start]));
        }
        else
        {
            // cout << start << " " << n - 1 << endl;
            ans.push_back(to_string(nums[start]) + "->" + to_string(nums[n - 1]));
        }


        return ans;
    }
};