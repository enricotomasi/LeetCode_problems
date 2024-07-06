class Solution 
{
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        int n = nums.size();
        unordered_map<int, vector<int>> num;

        for (int i = 0; i < n; i++)
        {
            num[nums[i]].push_back(i);
        }

        sort(nums.begin(), nums.end());

        int start = 0;
        int end = n - 1;

        while (start < end)
        {
            // cout << "start: " << start << " end: " << end << " nums[start]: " << nums[start] << "  nums[end]: " << nums[end] << " sum:" <<  (nums[start] + nums[end]) << " target: " << target << endl;

            if (nums[start] + nums[end] == target)
            {
                cout << "Bingo!" << endl;
                int first = -1;
                auto it = num.find(nums[start]);
                if (it != num.end())
                {
                    first = it->second[0];
                }

                int second = -1;
                it = num.find(nums[end]);
                if (it != num.end())
                {
                    if (it->second[0] != first)
                    {
                        second = it->second[0];
                    }
                    else
                    {
                        second = it->second[1];
                    }
                }

                return { first, second };
            }
            else if (nums[start] + nums[end] > target)
            {
                end--;
            }
            else
            {
                start++;
            }
        }

        return { -1 , -1 };
    }

};