class Solution
{
public:
    bool isPowerOfThree(int n)
    {
        if (n == 1)
        {
            return true;
        }

        long long int pot = 1;
        int i = 1;
        
        while (pot < n)
        {
            pot = pow(3, i);
            
            // cout << i << "# " << pot << endl;
            
            if (pot == n)
            {
                return true;
            }

            i++;
        }

        return false;

    }
};