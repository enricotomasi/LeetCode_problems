class Solution 
{
public:
    int searchInsert(vector<int>& nums, int target) 
    {
        int n = nums.size();

        if (nums[0] > target)
        {
            return 0;
        }
        
        if (n < 10)
        {
            for (int i = 0; i < n; i++)
            {
                if (nums[i] >= target)
                {
                    return i;
                }
            }
        }

        int mid = -1;

        int start = 0;
        int end = nums.size();

        while (start < end)
        {
            mid = (start + end) / 2;

            if (nums[mid] == target)
            {
                return mid;
            }
            
            if (nums[mid] > target)
            {
                end = mid - 1;
            }
            else
            {
                start = mid + 1;
            }
        }

        return mid + 1;

    }
};