class Solution
{
public:
    bool rotateString(string s, string goal)
    {
        int n = s.length();

        if (n != goal.length())
        {
            return false;
        }    

        for (int i = 0; i < n; i++)
        {
            if (s[i] == goal[0])
            {
                bool ok = true;

                int pos = (i + 1) % n;

                for (int j = 1; j < n; j++)
                {
                    if (goal[j] != s[pos])
                    {
                        ok = false;
                        break;
                    }

                    pos++;
                    pos %= n;
                }

                if (ok)
                {
                    return true;
                }

            }
        }

        return false;
    }
};