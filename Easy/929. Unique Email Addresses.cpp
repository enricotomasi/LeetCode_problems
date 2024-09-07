class Solution
{
public:
    int numUniqueEmails(vector<string> &emails)
    {
        set<string> mails;

        for (auto it : emails)
        {
            string name = "";
            string domain = "";

            bool dom = false;
            bool plus = false;

            for (char c : it)
            {
                if (c == '@')
                {
                    dom = true;
                }
                else if (dom)
                {
                    domain += c;
                }
                else if (!plus) // name
                {
                    
                    if (c == '+')
                    {
                        plus = true;
                    }
                    else if (c != '.')
                    {
                        name += c;
                    }
                }
            }

            string toins = name + "@" + domain;
            mails.insert(toins);
        }

        // for (auto it : mails) cout << it << endl; // Debug
        
        return mails.size();

    }
};