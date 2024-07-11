class Solution 
{
public:
    int removeDuplicates(vector<int>& nums) 
    {
        int ans = nums.size();
        
        if (ans == 1)
        {
            return ans;
        } 

        if (ans == 2)
        {
            if (nums[0] == nums[1])
            {
                return 1;
            }
            return ans;
        }
        
        int i = 0;
        
        bool change = false;
        while (i < ans)
        {
            // cout << endl << nums[i] << " " << nums[i + 1] << " ans: " << ans << endl;
            if (!change && i == ans - 1)
            {
                break;
            }
            
            if (nums[i] == nums[i + 1])
            {
                change = true;
                ans--;
                for (int j = i + 1; j < ans; j++)
                {
                    nums[j] = nums[j + 1];
                }
            }
            else
            {
                i++;
            }

            // for (auto it: nums) cout << it << " ";
            // cout << endl;

        }

        if (change)
        {
            ans++;
        }

        return ans;
    }
};