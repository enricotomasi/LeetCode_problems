class Solution
{
public:
    vector<int> addToArrayForm(vector<int> &num, int k)
    {
        int carry = 0;
        int pos = num.size() - 1;

        vector<int> ans;

        while (k || carry || pos >= 0)
        {
            // cout << endl << "pos: " << pos << " k: " << k << " carry: " << carry << endl;

            int a = carry;
            
            // cout << "a += carry: " << a << endl;
            
            if (pos >= 0)
            {
                a += num[pos];
                // cout << "pos > 0, a += num[pos]" << a << endl;
            }
            if (k > 0)
            {
                a += k % 10;
                // cout << "k > 0, a += k % 10 " << a << endl;
            }
            
            if (a < 9)
            {
                ans.push_back(a);
                carry = 0;
            }
            else
            {
                ans.push_back(a % 10);
                carry = a / 10;
            }

            k /= 10;
            pos--;
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};