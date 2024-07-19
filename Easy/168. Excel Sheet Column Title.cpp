class Solution
{
public:
    string convertToTitle(int columnNumber)
    {
        int n = columnNumber;
        string ans = "";

        while (n)
        {
            int rem = n % 26;
            char c = rem + 'A' - 1;

            if (rem == 0)
            {
                c = 'Z';
                n--;
            }

            //cout << "n: " << " rem:" << rem << " c: " << c << endl;

            ans = c + ans;

            n /= 26;
        }

        return ans;


    }
};