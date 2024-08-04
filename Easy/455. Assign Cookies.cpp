class Solution
{
public:
    int findContentChildren(vector<int> &g, vector<int> &s)
    {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int ng = g.size();
        int ns = s.size();

        int skip = ng - ns;

        int head = 0;
        int tail = ns - 1;

        int ans = 0;

        for (int i = ng - 1; i >= 0; i--)
        {
            // cout << i << "# " << g[i] << endl;
            // cout << "tail: " << tail << " head: " << head << endl;

            if (tail <= 0 && head >= ns)
            {
                break;
            }

            if (tail >= 0 && g[i] <= s[tail])
            {
                ans++;
                tail--;
            }
            else
            {
                if (skip > 0)
                {
                    skip--;
                }
                else
                {
                    head++;
                }
            }
        }

        return ans;
    }
};