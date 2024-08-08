class Solution
{
public:
    int fib(int n)
    {
        if (n == 0)
        {
            return 0;
        }
        
        if (n <= 2)
        {
            return 1;
        }
        
        int a = 1;
        int b = 1;
        int fibo = 1;

        for (int i = 2; i < n; i++)
        {
            fibo = a + b;
            a = b;
            b = fibo;
        }

        return fibo;
    }
};