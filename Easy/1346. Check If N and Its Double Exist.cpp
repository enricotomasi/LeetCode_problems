class Solution
{
public:
    bool checkIfExist(vector<int> &arr)
    {
        unordered_set<int> s;
        bool zero = false;
        bool one = false;
        
        for (auto it : arr)
        {
            if (it == 0 && !zero)
            {
               zero = true; 
            }
            else if (it == 1 && !one)
            {
                one = true;
            }
            else
            {
                s.insert(it);
            }
        }

        for (auto it : arr)
        {
            if (s.find(it + it) != s.end())
            {
                return true;
            }
        }

        return false;

    }
};