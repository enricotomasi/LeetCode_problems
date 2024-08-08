class Solution
{
public:
    bool detectCapitalUse(string word)
    {
        int cap = 0;
        int nocap = 0;

        for (char c : word)
        {
            if (c >= 'a' && c <= 'z')
            {
                nocap++;
            }
            else if (c >= 'A' && c <= 'Z')
            {
                cap++;
            }
        }

        if (cap == 0 || nocap == 0)
        {
            return true;
        }

        if (cap != 1)
        {
            return false;
        }

        if (word[0] >= 'A' && word[0] <= 'Z')
        {
            return true;
        }

        return false;

    }
};