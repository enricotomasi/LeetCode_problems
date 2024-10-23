class Solution
{
public:
    int maximum69Number (int num)
    {
        string temp = to_string(num);

        string ans = "";
        bool jolly = true;

        for (char c : temp)
        {
            if (c == '6' && jolly)
            {
                jolly = false;
                ans += '9';
            }
            else
            {
                ans += c;
            }
        }    


        return stoi(ans);
    }
};
