class Solution
{
public:
    uint32_t reverseBits(uint32_t n)
    {
        
        string bin = "";

        while (n)
        {
            bin += (n % 2) + '0';
            n /= 2;
        }

        int nb = bin.length();
        for (int i =  nb; i < 32; i++)
        {
            bin += '0';
        }

        cout << bin << endl;

        long long int ans = 0;

        for (int i = 0; i < 32; i++)
        {
            if (bin[i] == '1')
            {
                ans += pow(2, 31 - i);
            }
        }

        return (uint32_t)ans;
    }
};