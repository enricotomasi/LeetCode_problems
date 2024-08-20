class Solution
{
public:
    int findLengthOfLCIS(vector<int> &nums)
    { 
        int last = INT_MIN;
        int temp = 0;
        int ans = 0;

        for (auto it : nums)
        {
            // cout << endl << it << " last: " << last << endl;
            // cout << "ans: " << ans << " temp: " << temp << endl;

            if (it > last)
            {
                // cout << "it > last" << endl;
                temp++;
            }
            else
            {
                // cout << "it < last" << endl;
                ans = max(ans, temp);
                temp = 1;
            }
            
            // cout << "ans: " << ans << " temp: " << temp << endl;
            last = it;
        }

        return max(ans, temp);
        
    }
};