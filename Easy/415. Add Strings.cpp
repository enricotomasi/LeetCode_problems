class Solution
{
public:
    string addStrings(string num1, string num2)
    {
        int i1 = num1.length() - 1;
        int i2 = num2.length() - 1;

        string ans = "";
        int carry = 0;

        while (i1 >= 0 || i2 >= 0)
        {
            // cout << endl << "----------------------" << endl;
            // cout << "i1    : " << i1 << endl;
            // cout << "i2    : " << i2 << endl << endl;
            
            int r = 0;
            if (i1 < 0)
            {
                // cout << "i1 < 0" << endl;

                int d2 = num2[i2] - '0';
                r = d2 + carry;

                // cout << "d2    : " << d2 << endl;

                i2--;
            }
            else if (i2 < 0)
            {
                // cout << "i2 < 0" << endl;

                int d1 = num1[i1] - '0';
                r = d1 + carry;

                // cout << "d1    : " << d1 << endl;

                i1--;
            }
            else
            {
                cout << "i1 >= 0 && i2 >= 0" << endl;

                int d1 = num1[i1] - '0';
                int d2 = num2[i2] - '0';
                r = d1 + d2 + carry;
                
                // cout << "d1    : " << d1 << endl;
                // cout << "d2    : " << d2 << endl;

                i1--;
                i2--;
            }

            // cout << "rbefor: " << r << endl;
            if (r > 9)
            {
                carry = r / 10;
                r %= 10;
                
            }
            else
            {
                carry = 0;
            }
            // cout << "r     : " << r << endl;
            // cout << "carry : " << carry << endl;
           
            ans = to_string(r) + ans;

            // cout << endl << "ans   : " << ans << endl;
            // cout << "i1    : " << i1 << endl;
            // cout << "i2    : " << i2 << endl;

        }

        if (carry > 0)
        {
            ans = to_string(carry) + ans;
        }

        return ans;

    }
};