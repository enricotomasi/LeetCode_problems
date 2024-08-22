class Solution
{
public:
    bool hasAlternatingBits(int n)
    {
        bool zero = false;
        if (n % 2 == 0)
        {
            zero = true;
        }

        n /= 2;

        while (n)
        {
            if ((zero && n % 2 == 0) || (!zero && n % 2 == 1))
            {
                return false;
            }

            zero = !zero;
            n /= 2;
        }

        return true;
    }
};