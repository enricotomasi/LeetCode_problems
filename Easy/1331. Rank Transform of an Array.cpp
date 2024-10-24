class Solution
{
public:
    vector<int> arrayRankTransform(vector<int> &arr)
    {
        int n = arr.size();
        vector<int> arr2(arr);
        sort(arr2.begin(), arr2.end());
        
        int last = INT_MIN;
        int count = 1;
        unordered_map<int, int> m;

        for (int i = 0; i < n; i++)
        {
            if (arr2[i] != last)
            {
                m[arr2[i]] = count;
                count++;
            }
            
            last = arr2[i];
        }

        vector<int> ans;

        for (auto it : arr)
        {
            ans.push_back(m[it]);
        }

        return ans;


    }
};