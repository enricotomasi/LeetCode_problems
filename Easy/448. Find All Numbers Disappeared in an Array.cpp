class Solution
{
public:
    vector<int> findDisappearedNumbers(vector<int> &nums)
    {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        vector<int> ans;

        int pos = 0;
        int i = 1; 

        while (i <= n)
        {
            // cout << endl << "----------------------------------------" << endl;
            // cout << i << "# ";
            // if (pos < n) cout << "pos: " << pos << " nums[pos]: " << nums[pos];
            // cout << endl;

            if (pos >= n)
            {
                // cout << "pos >= n -1, add: " << i << endl;
                ans.push_back(i);
                i++;
            }
            else if (nums[pos] != i)
            {
                // cout << "nums[pos] != i" << endl;
                if (nums[pos] < i)
                {
                    // cout << "nums[pos] < i, pos++" << endl;
                    pos++;
                }
                else
                {
                    // cout << "else , add: " << i << " i++" << endl;
                    ans.push_back(i);
                    i++;
                }
            }
            else
            {
                // cout << "match!, pos++" << endl;
                pos++;
                i++;
            }
        }


        return ans;
    }
};