class Solution
{
public:
    int tribonacci(int n)
    {
        if (n == 0) return 0;
        else if (n < 3) return 1;

        int a = 0;
        int b = 1;
        int c = 1;
        int ans = 2;

        for (int i = 3; i <= n; i++)
        {
            ans = a + b + c;
            a = b;
            b = c;
            c = ans;
        }

        return ans;

    }
};