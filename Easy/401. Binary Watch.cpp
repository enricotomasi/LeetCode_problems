class Solution
{
public:
    static int cb(int n)
    {
        int ans = 0;
        
        while (n)
        {
            if (n % 2 == 1)
            {
                ans++;
            }

            n /=2;
        }

        return ans;
    } 
    vector<string> readBinaryWatch(int turnedOn)
    {
        int n = turnedOn;

        vector<string> ans;
        
        if (n >= 9)
        {
            return ans;
        }

        int hour[] = {8, 4, 2, 1};
        int min[] = {32, 16, 8, 4, 2, 1};

        unordered_map<int, int> setbits;

        for (int i = 0; i < 60; i++)
        {
            setbits[i] = cb(i);
        }
        
        for (int i = 0; i <= 11; i++)
        {
            int bith = setbits[i];
            for (int j = 0; j <= 59; j++)
            {
                //cout << i << " : " << j << "  cb(i): " << cb(i) << " cb(j)" << cb(j) << endl;
                int bits = bith + setbits[j];
                if (bits == n)
                {
                    string temp = "";
                    
                    temp += to_string(i);
                    
                    temp += ":";
                    
                    if (j <= 9)
                    {
                        temp += '0';
                    }
                    
                    temp += to_string(j);

                    ans.push_back(temp);
               
                }
            }
        }

        return ans;
    }
};