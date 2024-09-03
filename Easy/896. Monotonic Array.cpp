class Solution
{
public:
    bool isMonotonic(vector<int> &nums)
    {
        int n = nums.size();

        if (n == 1)
        {
            return true;
        }

        int j = 0;
        
        while (j < n - 1 && nums[j] == nums[j + 1])
        {
            j++;
        }
        
        if (j == n - 1)
        {
            return true;
        }

        if (nums[j] > nums[j + 1])
        {
            for (int i = 1; i < n - 1; i++)
            {
                if (nums[i] < nums[i + 1])
                {
                    return false;
                }
            }
        }    
        else
        {
            for (int i = 1; i < n - 1; i++)
            {
                if (nums[i] > nums[i + 1])
                {
                    return false;
                }
            }
        }

        return true;

    }
};
