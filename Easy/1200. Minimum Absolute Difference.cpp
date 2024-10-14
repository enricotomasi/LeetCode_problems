class Solution
{
public:
    vector<vector<int>> minimumAbsDifference(vector<int> &arr)
    {
        int n = arr.size();
        sort(arr.begin(), arr.end());
        
        int abdi = INT_MAX;
        
        for (int i = 0; i < n - 1; i++)
        {
            abdi = min(abdi, abs(arr[i] - arr[i + 1]));
        }

        // cout << "abdi: " << abdi << endl;
        
        vector<vector<int>> ans;

        for (int i = 0; i < n - 1; i++)
        {
            // cout << arr[i] << " " << arr[i + 1] << " " << (abs(arr[i] - arr[i + 1])) << endl;
            if (abs(arr[i] - arr[i + 1]) == abdi)
            {
                // cout << "bingo!" << endl;
                ans.push_back({arr[i], arr[i + 1]});
            }
        }

        // sort(ans.begin(), ans.end());

        return ans;

    }
};
