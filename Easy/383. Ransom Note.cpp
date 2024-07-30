class Solution
{
public:
    bool canConstruct(string ransomNote, string magazine)
    {
        vector<int> ranmap(26, 0);

        for (auto it : magazine)
        {
            ranmap[it - 'a']++;
        }

        for (auto it : ransomNote)
        {
            if (ranmap[it - 'a'] <= 0)
            {
                return false;
            }

            ranmap[it - 'a']--;
        }

        return true;

    }
};