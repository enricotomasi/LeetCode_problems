class Solution
{
public:
    bool lemonadeChange(vector<int> &bills)
    {
        int five = 0;
        int ten = 0;

        for (auto it : bills)
        {
            // cout << endl << "pay with: " << it << "$" << endl;
            // cout << "5$ : " << five << " 10$ : " << ten << endl; 
            if (it == 5)
            {
                five++;
            }
            else if (it == 10)
            {
                ten++;
                if (five >= 1)
                {
                    five--;
                }
                else
                {
                    return false;
                }

            }
            else // 20
            {
                if (ten >= 1 && five >= 1)
                {
                    ten--;
                    five--;
                }
                else if (five >= 3)
                {
                    five -= 3;
                }
                else
                {
                    return false;
                }
            }

            // cout << "5$ : " << five << " 10$ : " << ten << endl; 
        }

        return true;
    }
};