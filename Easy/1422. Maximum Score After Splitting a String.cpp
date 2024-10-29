class Solution
{
public:
    int maxScore(string s)
    {
        int startzero = 0;
        int startone = 0;

        int endzero = 0;
        int endone = 0;

        for (auto c : s)
        {
            if (c == '0')
            {
                endzero++;
            }
            else
            {
                endone++;
            }
        }

        // cout << "endzero: " << endzero << " endone: " << endone << endl;

        int ans = 0;

        int n = s.size();
        for (int i = 0; i < n - 1; i++)
        {
            char c = s[i];
            if (c == '0')
            {
                startzero++;
                endzero--;
            }
            else
            {
                startone++;
                endone--;
            }

            ans = max(ans, (startzero + endone));
            
            // cout << endl << c << endl;
            // cout << "startzero: " << startzero << " startone: " <<  startone << endl;
            // cout << "endzero: " << endzero << " endone: " << endone << endl;
            // cout << "startzero+endone: " << (startzero + endone) << endl;
            // cout << "ans: " << ans << endl;

        }


        return ans;
    }
};
