class Solution
{
public:
    bool canThreePartsEqualSum(vector<int> &arr)
    {
        int sum = 0;

        for (auto it : arr)
        {
            sum += it;
        }

        if (sum % 3 != 0)
        {
            return false;
        }
  
        int temp = 0;
        int c = 0;

        for (auto it : arr)
        {
            temp += it;

            if (temp == (c + 1) * sum / 3)
            {
                c++;
            }
        }
        
        return c >= 3;
    }
};
