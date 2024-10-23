class Solution
{
public:
    bool checkzero(int n)
    {
        while (n)
        {
            if (n % 10 == 0)
            {
                return false;
            }

            n /= 10;
        }
        return true;
    }
    
    vector<int> getNoZeroIntegers(int n)
    {
        if (n == 2) return {1, 1};
     
        vector<int> ans;

        int start = 1;
        int end = n - 1;

        while (start < end)
        {
            if (checkzero(start) && checkzero(end))
            {
                return {start, end};
            }
            start++;
            end--;
        }

        return {-1, -1};
    }
};
