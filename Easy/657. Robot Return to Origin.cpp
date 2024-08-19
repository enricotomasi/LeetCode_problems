class Solution
{
public:
    bool judgeCircle(string moves)
    {
        int x = 0;
        int y = 0;

        for (auto it : moves)
        {
            if (it == 'U')
            {
                x--;
            }
            else if (it == 'D')
            {
                x++;
            }
            else if (it == 'L')
            {
                y--;
            }
            else
            {
                y++;
            }
        }    

        return x == 0 && y == 0;
    }
};