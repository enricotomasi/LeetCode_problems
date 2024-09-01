class Solution
{
public:
    int binaryGap(int n)
    {
        int pos = 0;
        int last = 100000000000;

        int ans = 0;

        while (n)
        {
            if (n % 2 == 1)
            {
                ans = max(ans, (pos - last));
                last = pos;
            }

            pos++;
            n /= 2;
        }

        return ans;

    }
};