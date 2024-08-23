class Solution
{
public:
    int findShortestSubArray(vector<int> &nums)
    {
        int n = nums.size();

        map<int, int> m;

        for (auto it : nums)
        {
            m[it]++;
        }

        int mm = INT_MIN;

        // cout << "map: " << endl;
        for (auto it : m)
        {
            // cout << it.first << " " << it.second << endl;
            mm = max(mm, it.second);
        } 

        // cout << endl << "maximum: " << mm << endl;
        
        // cout << endl << "degrees: ";

        unordered_set<int> d;
        for (auto it : m)
        {
            if (it.second == mm)
            {
                // cout << it .first << " ";
                d.insert(it.first);
            }
        }
        // cout << endl;

        int start;

        for (start = 0; start < n; start++)
        {
            if (d.find(nums[start]) != d.end())
            {
                break;
            }
        }

        int ans = INT_MAX;
        for (auto it : d)
        {
            int start;

            for (start = 0; start < n; start++)
            {
                if (nums[start] == it)
                {
                    break;
                }
            }

            int end;

            for (end = n - 1; end >= 0; end--)
            {
                if (nums[end] == it)
                {
                    break;
                }
            }
            
            ans = min(ans, (end - start + 1));
        }

        return ans;
    }
};