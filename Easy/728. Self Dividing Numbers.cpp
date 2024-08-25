
class Solution
{
public:
    bool sd(int n)
    {
        int copy = n;
        while (copy)
        {
            int digit = copy % 10;

            if (digit == 0 || n % digit != 0)
            {
                return false;
            }

            copy /= 10;
        }

        return true;
    }
    
    vector<int> selfDividingNumbers(int left, int right)
    {
        vector<int> ans;

        for (int i = left; i <= right; i++)
        {
            if (sd(i))
            {
                ans.push_back(i);
            }
        }

        return ans;
    }
};