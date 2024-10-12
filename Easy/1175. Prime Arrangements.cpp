class Solution
{
public:
    int numPrimeArrangements(int n)
    {
        int m = 1000000007;

        vector<bool> sieve(n + 1, true);
        sieve[0] = false;
        sieve[1] = false;

        for (int i = 2; i <= sqrt(n); i++)
        {
            if (sieve[i])
            {
                for (int j = i + i; j <= n; j += i)
                {
                    sieve[j] = false;
                }
            }
        }

        int primes = 0;

        for (int i = 0; i <= n; i++)
        {
            if (sieve[i])
            {
                // cout << i << " ";
                primes++;
            } 
        } 
        
        // cout << endl << "primes: " << primes << " n - primes: " << (n - primes) << endl; 
        
        long long int ans = 1;
        for (int i = 1; i <= primes; i++)
        {
            ans = (ans * i) % m;
        }

        for (int i = 1; i <= n - primes; i++)
        {
            ans = (ans * i) % m;
        }

        return (int)ans;
    }
};