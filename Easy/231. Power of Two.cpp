class Solution
{
public:
    bool isPowerOfTwo(int n)
    {
        if (n <= 0)
        {
            return false;
        }
        
        double l = log2(n);

        return l - (long long int)l == 0;

    }
};