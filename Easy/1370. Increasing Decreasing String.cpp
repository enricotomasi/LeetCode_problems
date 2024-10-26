class Solution
{
public:
    string sortString(string s)
    {
        int n = s.length();

        vector<char> v;
        for (char c : s)
        {
            v.push_back(c);
        }

        sort(v.begin(), v.end());

        int arr[26] = {};
        for (char c : v)
        {
            arr[c - 'a']++;
        }

        // for (int i = 0; i < 26; i++) cout << (char)(i + 'a') << " " << arr[i] << endl; // debug

        bool allzero = false;
        string ans = "";
        
        while (!allzero)
        {
            allzero = true;
            
            for (int i = 0; i < 26; i++) // pass 1 - 2
            {
                if (arr[i] != 0)
                {
                    allzero = false;
                    ans += i + 'a';
                    arr[i]--;
                }
            }

            for (int i = 25; i >= 0; i--)
            {
                if (arr[i] != 0)
                {
                    allzero = false;
                    ans += i + 'a';
                    arr[i]--;
                }
            }
        }

        return ans;

    }
};