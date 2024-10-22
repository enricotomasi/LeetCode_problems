class Solution
{
public:
    int subtractProductAndSum(int n)
    {
        long long int prod = 1;
        long long int sum = 0;

        while (n)
        {
            int digit = n % 10;
            prod *= digit;
            sum += digit;

            n /= 10;
        }

        return (int)(prod - sum);
        
    }
};
