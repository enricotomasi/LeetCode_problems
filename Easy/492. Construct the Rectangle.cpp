class Solution
{
public:
    vector<int> constructRectangle(int area)
    {
        int l = -10000001;
        int w = 10000001;

        for (int i = 0; i < area; i++)
        {
            for (int j = 0; j < area; j++)
            {
                int a = i * j;
                if (a > area)
                {
                    break;
                }

                if (a == area && abs(l - w) > abs(i - j))
                {
                    l = i;
                    w = j;
                }
            }
        }

        if (l == -10000001 || w == 10000001)
        {
            return { area, 1};
        }

        if (l > w)
        {
            return { l, w };
        }

        return { w, l };
    }
};