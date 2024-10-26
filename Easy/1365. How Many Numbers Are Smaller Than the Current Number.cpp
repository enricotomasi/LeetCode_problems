class Solution
{
public:
    vector<int> smallerNumbersThanCurrent(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> copy(nums);
        sort(copy.begin(), copy.end());

        unordered_map<int, int> m;
        m[copy[0]] = 0;
        int great = 0;
        int great2 = 1;

        for (int i = 1; i < n; i++)
        {
            if (copy[i] != copy[i - 1])
            {
                m[copy[i]] = great2;
                great = great2;
            } 
            else
            {
               m[copy[i]] = great;
            }
            great2++;
        }

        // for (auto it : m) cout << it.first << ": " << it.second << endl;

        vector<int> ans;

        for (auto it : nums)
        {
            ans.push_back(m[it]);
        }

        return ans;

    }
};