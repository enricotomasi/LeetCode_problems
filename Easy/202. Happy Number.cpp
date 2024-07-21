class Solution
{
public:
    bool isHappy(int n)
    {
        int c = 0;
        while (n != 1)
        {
            //cout << "n: " << n << endl;

            int temp = 0;
            while (n)
            {
                temp += pow(n % 10, 2);
                n /= 10;
            }

            n = temp;

            if (c > 150)
            {
                return false;
            }

            c++;
        }

        return true;

    }
};