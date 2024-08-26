class Solution
{
public:
    int countsetbits(int n)
    {
        int ans = 0;

        while (n)
        {
            if (n % 2 == 1)
            {
                ans++;
            }

            n /= 2;
        }

        return ans;
    }

    int countPrimeSetBits(int left, int right)
    {
        set<int> primes({2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31});
        int ans = 0;

        for (int i = left; i <= right; i++)
        {
            if (primes.find(countsetbits(i)) != primes.end())
            {
                ans++;
            }

        }

        return ans;
    }
    
};