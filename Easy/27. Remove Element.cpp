class Solution 
{
public:
    int removeElement(vector<int>& nums, int val) 
    {
        int n = nums.size();
        
        if (n == 1)
        {
            if (nums[0] == val)
            {
                return 0;
            }
            
            return 1;
        }
        
        int pos = n - 1;
        int ans = 0;

        for (int i = 0; i < n; i++)
        {
            if (nums[i] == val)
            {
                while (pos > 0 && nums[pos] == val)
                {
                    pos--;
                }

                if (pos < 0)
                {
                    return ans;
                }
                
                nums[i] = nums[pos];
                pos--;
            }
            else
            {
                ans++;
            }

        }

        return ans;

    }
};