class Solution 
{
public:
    int climbStairs(int n) 
    {
        if (n == 1)
        {
            return 1;
        }
        
        
        int a = 1;
        int b = 1;
        int fibo = 2;

        for (int i = 1; i < n; i++)
        {
            fibo = a + b;
            a = b;
            b = fibo;
        }

        return fibo;
    }
};