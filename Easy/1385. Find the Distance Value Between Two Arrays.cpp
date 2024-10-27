class Solution
{
public:
    int findTheDistanceValue(vector<int> &arr1, vector<int> &arr2, int d)
    {
        sort(arr2.begin(), arr2.end());

        int ans = 0;
        
        for (auto num : arr1)
        {
            auto it = lower_bound(arr2.begin(), arr2.end(), num);
            bool ok = true;

            if ((it == arr2.end() || abs(*it - num) > d) && (it == arr2.begin() || abs(*(it - 1) - num) > d))
            {
                ans++; 
            }

        }

        return ans;
    }
};