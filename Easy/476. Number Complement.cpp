class Solution
{
public:
    int findComplement(int num)
    {
        int ans = 0;
        int p = 0;

        while (num)
        {
            if (num % 2 == 0)
            {
                ans += pow(2, p);
            }
            
            p++;
            num /= 2;
        }

        return ans;






        return 42;

    }
};