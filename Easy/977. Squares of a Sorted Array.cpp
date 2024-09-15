class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        vector<int> ans;
        
        int n = nums.size();
        // cout << "n: " << n << endl;

        if (n < 5)
        {
            for (auto it : nums)
            {
                ans.push_back(it * it);
            }

            sort(ans.begin(), ans.end());
            return ans;
        }

        int start = 0;
        int end = n - 1;
        int mid;

        while (start <= end)
        {
            mid = (start + end) / 2;
            if (nums[mid] == 0)
            {
                break;
            }
            else if (nums[mid] > 0)
            {
                end = mid - 1;
            }
            else
            {
                start = mid + 1;
            }
        }

        // cout << "mid: " << mid << " nums[mid]: " << nums[mid] << endl;

        if (mid < n - 1 && abs(nums[mid]) > abs(nums[mid + 1]))
        {
            mid++;
        }
        else if (mid > 0 && abs(nums[mid]) > abs(nums[mid - 1]))
        {
            mid--;
        }
         
        // cout << "mid: " << mid << " nums[mid]: " << nums[mid] << endl;
  
        ans.push_back(nums[mid] * nums[mid]);

        int a = mid - 1;
        int b = mid + 1;
        
        while (a >= 0 || b < n)
        {
            // cout << endl << "a: " << a << " b: " << b << endl; 
            if (a < 0)
            {
                // cout << "a < 0 *** take b" << endl;
                ans.push_back(nums[b] * nums[b]);
                b++;
            }
            else if (b >= n)
            {
                // cout << "b >= n *** take a" << endl;
                ans.push_back(nums[a] * nums[a]);
                a--;
            }
            else
            {
                // cout << "else" << endl;
                if (abs(nums[a]) <= abs(nums[b]))
                {
                    // cout << "abs(nums[a]) <= abs(nums[b]) *** take a" << endl;
                    ans.push_back(nums[a] * nums[a]);
                    a--;
                }
                else
                {
                    // cout << "abs(nums[a]) > abs(nums[b]) *** take b" << endl;
                    ans.push_back(nums[b] * nums[b]);
                    b++;
                }
            }
        }
        
        return ans;
        
    }
};