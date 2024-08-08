class Solution
{
public:
    bool checkPerfectNumber(int num)
    {
        if (num == 1)
        {
            return false;
        }
        
        int div = 1;
        int copy = num;

        for (int i = 2; i <= sqrt(num); i++)
        { 
            // cout << i << "# " ;
            if (num % i == 0)
            {
                div += i;

                // cout << i << " ";

                if (num / i != i)
                {
                    div += num / i;
                    // cout << num / i << " ";
                }
            }

            // cout << endl;
        }

        return copy == div;
    }
};