class Solution
{
public:
    int numJewelsInStones(string jewels, string stones)
    {
        unordered_set<char> jew;

        for (char c : jewels)
        {
            jew.insert(c);
        }

        int ans = 0;

        for (char c : stones)
        {
            if (jew.find(c) != jew.end())
            {
                ans++;
            }
        }
        
        return ans;
    }
};