class Solution
{
public:
    vector<int> numberOfLines(vector<int> &widths, string s)
    {
        int lines = 1;
        int siz = 0;

        for (auto it : s)
        {
            int l = widths[it - 'a']; 
            if (siz + l > 100)
            {
                lines++;
                siz = l;
            }
            else
            {
                siz += l;
            }
        }

        return {lines, siz};
    }
};