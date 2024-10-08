class Solution
{
public:
    bool canBeEqual(vector<int> &target, vector<int> &arr)
    {
        int n = arr.size();
        if (n != target.size())
        {
            return false;
        }

        sort(arr.begin(), arr.end());
        sort(target.begin(), target.end());

        for (int i = 0; i < n; i++)
        {
            if (arr[i] != target[i])
            {
                return false;
            }
        }

        return true;

    }
};