class Solution
{
public:
    int minTimeToVisitAllPoints(vector<vector<int>> &points)
    {
        int n = points.size();
        int ans = 0;

        for (int i = 0; i < n - 1; i++)
        {
            int x1 = points[i][0];
            int y1 = points[i][1];

            int x2 = points[i + 1][0];
            int y2 = points[i + 1][1];

            int dist = 0;

            // cout << endl << "   *** " << x1 << ", " << y1 << " " << x2 << ", " << y2 << endl;

            while (x1 != x2 || y1 != y2)
            {
                if (x1 == x2)
                {
                    if (y1 > y2) y1--;
                    else y1++;
                }
                else if (y1 == y2)
                {
                    if (x1 > x2) x1--;
                    else x1++;
                }
                else
                {
                    if (x1 > x2) x1--;
                    else x1++;

                    if (y1 > y2) y1--;
                    else y1++;
                }
                dist++;
                // cout << x1 << ", " << y1 << " " << x2 << ", " << y2 << "   *** dist: " << dist << endl;;
            }

            ans += dist;
        }
        
        return ans;
    }
};