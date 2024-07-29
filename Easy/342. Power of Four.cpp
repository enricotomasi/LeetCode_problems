class Solution
{
public:
    bool isPowerOfFour(int n)
    {
        if (n == 1 || n == 4)
        {
            return 4;
        }
        
        long long int p = 4;

        while (p < n)
        {
            p *= 4;
            
            if (p == n)
            {
                return true;
            }
        }

        return false;
    }
};