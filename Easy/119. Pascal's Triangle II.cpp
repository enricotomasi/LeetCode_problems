class Solution 
{
public:
    vector<int> getRow(int rowIndex) 
    {   
        int n = rowIndex;
        vector<int> ans;

        if (n == 0) return { 1 }; 

        if (n == 1) return { 1, 1 };

        long long prev = 1;
        ans.push_back(prev);

        for (int i = 1; i <= n; i++)
        {
            long long curr = (prev * (n - i + 1)) / i;
            ans.push_back((int)curr);
            prev = curr;
        }

        return ans;
    }
};